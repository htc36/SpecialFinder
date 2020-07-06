import requests
import random
from bs4 import BeautifulSoup
import json
from databaseCommands import *
from initSession import *
import time
import math
import datetime

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

def runSections(s, links, cursor, storeId,date, name):
    s = setUpSession(s, storeId)
    base = 'https://www.paknsaveonline.co.nz'
    for link in links:
        data = s.get(base + link).content
        soup = BeautifulSoup(data, 'lxml')
        #maxPage = soup.find("div", {"class": "fs-product-filter__item u-color-half-dark-grey u-hide-down-l"}).text.split(" ")[-2]
        maxPage = soup.find("div", {"class": "fs-pagination__info"}).text.split(" ")[-2]
        maxPage = math.ceil((int(maxPage) / 20))
        departmentList = link.split("/")[2 : 5]

        for page in range(1, maxPage + 1):
            time.sleep(random.uniform(2,7))
            url = base + link + "?pg=" + str(page)
            print(url)
        #    print(soup.prettify())
            products = scrapeKeywords(s, url, departmentList, name)
            addToDatabase(products, cursor, date)

def scrapeKeywords(s, url, departmentList, name):
    soup = BeautifulSoup(s.get(url).content, 'lxml')
    items = soup.findAll("div", {"class": "fs-product-card"})
    resultsList = []
    print(name)
    for iii in items:
        try:
            productDetailsDict = json.loads(iii.find("div", {"class": "js-product-card-footer fs-product-card__footer-container"})['data-options'])
        except:
            raw = (iii.find("div", {"class": "js-product-card-footer fs-product-card__footer-container"})['data-options']).split('\n')
            productDetailsDict = fixJson(raw)
            continue

        productOutput = [iii.find("p", {"class": "u-color-half-dark-grey u-p3"}).text[0:7]]
        productOutput += [productDetailsDict['productId'], productDetailsDict['productName'][0:99]]

        priceSpec = productDetailsDict['ProductDetails']

        productOutput.append(priceSpec['PriceMode'][0:9])
        if priceSpec['HasMultiBuyDeal']:
            productOutput += [priceSpec['MultiBuyQuantity'], priceSpec['MultiBuyPrice'] ]
        else:
            productOutput += [None, priceSpec['PricePerItem'] ]
        resultsList.append(productOutput + departmentList + [name])
    return resultsList

def run():
    for name, storeId in getStores():
        s = requests.Session()
        s =setUpSession(s, storeId)
        del s.cookies["server_nearest_store"]
        connection = databaseConnect()
        links = getUrlLinks(s, storeId)
        cursor = connection.cursor()
        date = ((datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)).strftime("%d/%m/%y"))
        createTable(cursor, date)
        runSections(s, links, connection, storeId, date, name)

run()
