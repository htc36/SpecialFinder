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
                links.append(innerSection["URL"].split("?")[0])
            #types.update(set(innerSection["URL"].split('/')[2:4]))
#    addTypes(connection, list(types))
    return links


def runSections(s, links, cursor, storeId,date, name):
    s = setUpSession(s, storeId)
    base = 'https://www.paknsaveonline.co.nz'
    for link in links:
        print(time.localtime())
        print("inside " + link)
        data = s.get(base + link).content
        print(data)
        soup = BeautifulSoup(data, 'lxml')
        try:
            maxPage = soup.find("div", {"class": "fs-pagination__info"}).text.split(" ")[-2]
        except:
            print("find Page failed")
            maxPage = soup.find("div", {"class": "fs-product-filter__item u-color-half-dark-grey u-hide-down-l"}).text.split(" ")[-2]
        maxPage = math.ceil((int(maxPage) / 20))
        departmentList = link.split("/")[2 :]

        for page in range(1, maxPage + 1):
            time.sleep(random.uniform(7,20))
            # time.sleep(random.uniform(2,5))
            url = base + link + "?pg=" + str(page)
            print(url)
            productList, priceList = scrapeKeywords(s, url, departmentList, name, date)
            print(s.cookies["STORE_ID"])
            addToDatabase(productList, priceList, cursor)

def scrapeKeywords(s, url, departmentList, name, date):
    soup = BeautifulSoup(s.get(url).content, 'lxml')
    items = soup.findAll("div", {"class": "fs-product-card"})
    productList = []
    priceList = []
    for iii in items:
        try:
            productDetailsDict = json.loads(iii.find("div", {"class": "js-product-card-footer fs-product-card__footer-container"})['data-options'])
        except:
            raw = (iii.find("div", {"class": "js-product-card-footer fs-product-card__footer-container"})['data-options']).split('\n')
            productDetailsDict = fixJson(raw)
            continue

        product = [productDetailsDict['productId']]
        priceStoreDate = [productDetailsDict['productId']]

        product += [iii.find("p", {"class": "u-color-half-dark-grey u-p3"}).text[0:7]]
        product += [productDetailsDict['productName'][0:99]]

        priceSpec = productDetailsDict['ProductDetails']

        product.append(priceSpec['PriceMode'][0:9])
        if priceSpec['HasMultiBuyDeal']:
            priceStoreDate += [priceSpec['MultiBuyQuantity'], priceSpec['MultiBuyPrice'] ]
        else:
            priceStoreDate += [None, priceSpec['PricePerItem'] ]
        # print(product + departmentList)
        # print(priceStoreDate + [name, date])
        productList.append(product + departmentList)
        priceList.append(priceStoreDate + [name, date])
    return productList, priceList

def run():
    for name, storeId in getStores():
        print("NEW STORE = " + name)
        s = requests.Session()
        s =setUpSession(s, storeId)
        print(s.cookies["STORE_ID"])
        del s.cookies["server_nearest_store"]
        connection = databaseConnect()
        links = getUrlLinks(s, storeId)
        cursor = connection.cursor()
        date = ((datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)).strftime("%Y-%m-%d"))
        runSections(s, links, connection, storeId, date, name)
        print(name)
run()
