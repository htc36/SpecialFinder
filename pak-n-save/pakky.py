import requests
import random
from bs4 import BeautifulSoup
import json
from databaseCommands import *
from initSession import *
import time
import math

# Pushes request to Pak n Save API that retrieves the links to all the pages I want to scrape from on the website
def getUrlLinks(s, storeId):
    data = s.get('https://www.paknsaveonline.co.nz/CommonApi/Navigation/MegaMenu?v=2401&storeId=' + storeId).json()
    overallSections = (data['NavigationList'][0]["Children"])
    links = []
    types = set() 
    for section in overallSections:
        for innerSection in (section["Children"]):
            if (len(innerSection["Children"]) != 0):
                for bottomSection in innerSection['Children']:
                    links.append(bottomSection["URL"])
            else:
                links.append(innerSection["URL"])
            #types.update(set(innerSection["URL"].split('/')[2:4]))
#    addTypes(connection, list(types))
    return links

def runSections(s, links, cursor):
    base = 'https://www.paknsaveonline.co.nz'
    for link in links[17 : :]:
        soup = BeautifulSoup(s.get(base + link).content)

        #maxPage = soup.find("div", {"class": "fs-product-filter__item u-color-half-dark-grey u-hide-down-l"}).text.split(" ")[-2]
        print(link)
        maxPage = soup.find("div", {"class": "fs-pagination__info"}).text.split(" ")[-2]
        maxPage = math.ceil((int(maxPage) / 20))
        departmentList = link.split("/")[2 : 4]

        for page in range(1, maxPage + 1):
            time.sleep(random.uniform(2,7))
            url = base + link + "?pg=" + str(page)
            print(url)
            print(maxPage)
            print(soup.prettify())
            products = scrapeKeywords(s, url, departmentList)
            addToDatabase(products, cursor, 'testerLarge')

def scrapeKeywords(s, url, departmentList):
    soup = BeautifulSoup(s.get(url).content)
    items = soup.findAll("div", {"class": "fs-product-card"})
    resultsList = []
    for iii in items:
        productDetailsDict = json.loads(iii.find("div", {"class": "js-product-card-footer fs-product-card__footer-container"})['data-options'])
        print(len(productDetailsDict))
        productOutput = [iii.find("p", {"class": "u-color-half-dark-grey u-p3"}).text]
        productOutput += [(productDetailsDict['productId']), productDetailsDict['productName']]

        priceSpec = productDetailsDict['ProductDetails']

        productOutput.append(priceSpec['PriceMode'])
        if priceSpec['HasMultiBuyDeal']:
            productOutput += [priceSpec['MultiBuyQuantity'], priceSpec['MultiBuyPrice'] ]
        else:
            productOutput += [None, priceSpec['PricePerItem'] ]
        resultsList.append(productOutput + departmentList)
    return resultsList

def run():
    s = requests.Session()
    storeId ='65defcf2-bc15-490e-a84f-1f13b769cd22'
    s =setUpSession(s, storeId)
    print(s.cookies)
    del s.cookies["server_nearest_store"]

    
    connection = databaseConnect()
    links = getUrlLinks(s, storeId)
    cursor = connection.cursor()
    createTable(cursor, "testerLarge")
    #links = getUrlLinks(s)
    runSections(s, links, connection)

run()
