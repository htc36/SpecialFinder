import requests
import random
import math
import mysql.connector
import time
import re
import datetime
from databaseCommands import *
from urlFinder import *
from extraFunctions import *


def getData(url):
    time.sleep(random.uniform(2,4))
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'method': 'GET', 'accept-encoding': 'gzip, deflate, br', 'cache-control': 'no-cache', 'content-type': 'application/json', 'pragma': 'no-cache', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'x-requested-with': 'OnlineShopping.WebApp'}
    print(url)
    return requests.get(url, headers=headers)

def processData(connection, url, page, typee, date):
    # there is a 'dasFacets' which has data on how many multibuy or onecard specials etc
    #also facets which has details on what type of items are on sale
    response = getData(url)
    productDataList = []
    priceDataList = []
   # print(response.json())
    items = response.json()['products']['totalItems']
    products = response.json()['products']['items']
    for i in products:
        if (i['type'] != 'Product'):
            continue
        startIndex = len(i['brand'])+1
        name = i['name'][startIndex : ] 
        if typee == "liquor-beer-cider":
            amount = i['size']['packageType']
            amountInPack = i['size']['volumeSize']
            if amount == None:
                amount = i['variety']
            try:
                name += " " +  amountInPack
            except:
                pass
        productDetails = [name, i['brand'], i['price']['originalPrice'], i['price']['salePrice'], \
                i['size']['volumeSize'], None, 1, typee, i['sku']]
        if typee == "liquor-beer-cider":
            productDetails[4] = amount
        if i['productTag'] != None:
            productDetails[-4] = i['productTag']['tagType'] 
 
        if productDetails[-4] == "Other": 
            title = i['productTag']['additionalTag']['name']
            if re.search("(...)\s[0-9]+\sfor\s\$[0-9]+(...)", title):
                splitter = title.split()
                try:
                    productDetails[-3] = int(splitter[1])
                    productDetails[3] = int(splitter[3][1:])/int(splitter[1])
                except:
                    print("Multibuy finder did not work")
            elif re.search("[0-9]+\sfor\s\$[0-9]+(...)", title):
                splitter = title.split()
                try: 
                    productDetails[-3] = int(splitter[0])
                    
                    productDetails[3] = int(splitter[2][1:])/int(splitter[0])
                except:
                    print("multibuy finder failed number at start")

        if productDetails[-4] == 'IsMultiBuy' or productDetails[-4] == 'IsGreatPriceMultiBuy':
            productDetails[-3] = i['productTag']['multiBuy']['quantity']
            productDetails[3] = round(i['productTag']['multiBuy']['value'] / i['productTag']['multiBuy']['quantity'], 2)

        productDetails.append(i['barcode'])
        image = i["images"]["small"].split("/")[-1]
        productData = [productDetails[0], productDetails[1], productDetails[4], productDetails[7], productDetails[9], productDetails[8], image]
        priceData = [productDetails[2], productDetails[3], productDetails[5], productDetails[6], productDetails[8], date]
        productDataList.append(tuple(productData))
        priceDataList.append(tuple(priceData))
    addToDatabase2(productDataList, priceDataList, connection)
    maxPage = math.ceil(items / 120)
    
    if page < maxPage:
        page += 1
        editLocation = -15
        if page >= 11:
            editLocation = -16
        url = (url[: editLocation] + str(page) + '&target=browse')
        processData(connection, url, page, typee, date)


def main():
    # date = datetime.today().strftime('%Y-%m-%d')
    date = ((datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)).strftime("%Y-%m-%d"))
    connection = databaseConnect()
    cursor = connection.cursor()
    locations = departmentFinder()
    for iii in locations:
        page = 1
        url = 'https://shop.countdown.co.nz/api/v1/products/search?dasFilter=Department%3B%3B' + iii + '%3Bfalse&nextUI=true&size=120&page=1&target=browse'
        url = 'https://shop.countdown.co.nz/api/v1/products?dasFilter=Department%3B%3B' + iii + '%3Bfalse&nextUI=true&size=120&page=1&target=browse'
        processData(connection, url, page, iii, date)
    print("finished")
main()

