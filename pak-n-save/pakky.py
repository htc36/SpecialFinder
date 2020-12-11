import requests
import random
from bs4 import BeautifulSoup
import json
from databaseCommands import *
from initSession import *
import time
import math
import datetime
from traceback_with_variables import printing_tb, ColorSchemes

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
        print("trying to get max page of " + link)
        data = s.get(base + link).content
        soup = BeautifulSoup(data, 'lxml')
        if soup.find('title').text == ' PAKnSave - Error ':
            print("find Page failed" + "\n\n\n\n\n\n\n\n")
            time.sleep(random.uniforl(30,50))
            data = s.get(base + link).content
            soup = BeautifulSoup(data, 'lxml')
            maxPage = soup.find("div", {"class": "fs-pagination__info"}).text.split(" ")[-2]
        else:
            maxPage = soup.find("div", {"class": "fs-pagination__info"}).text.split(" ")[-2]
        maxPage = math.ceil((int(maxPage) / 20))
        departmentList = link.split("/")[2 :]

        for page in range(1, maxPage + 1):
            time.sleep(random.uniform(10,20))
            # time.sleep(random.uniform(2,5))
            url = base + link + "?pg=" + str(page)
            print(url + " " + s.cookies["STORE_ID"][0:5] + " " + name)
            productList, priceList = scrapeKeywords(s, url, departmentList, name, date)
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
            print("Load JSON FAILED")
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
        print("NEW STORE = " + name + "\n\n")
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
    print("I have completed!!!!!!")

def init():
    with printing_tb(
            num_context_lines=1,
            max_value_str_len=-1,
            max_exc_str_len=-1,
            ellipsis_='...',
            skip_cur_frame=False,  # e.g. no info about 'x'
            reraise=False,  # i.e. program won't fail, exceptions stay inside
            # color_scheme=ColorSchemes.synthwave,
    ):
        run()


init()