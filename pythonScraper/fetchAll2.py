import requests
import random
import math
import mysql.connector
import time
import re
from datetime import datetime
from databaseCommands import *

def getData(url):
    time.sleep(random.uniform(3,7))
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'method': 'GET', 'accept-encoding': 'gzip, deflate, br', 'cache-control': 'no-cache', 'content-type': 'application/json', 'pragma': 'no-cache', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'x-requested-with': 'OnlineShopping.WebApp'}
    return requests.get(url, headers=headers)

def processData(connection, url, page, typee, tableName):
    # there is a 'dasFacets' which has data on how many multibuy or onecard specials etc
    #also facets which has details on what type of items are on sale
    response = getData(url)
    productList = []
   # print(response.json())
    items = response.json()['products']['totalItems']
    products = response.json()['products']['items']
    for i in products:
        startIndex = len(i['brand'])+1
        name = i['name'][startIndex : ] 
        if typee == "liquor-beer-cider":
            amount = i['size']['packageType']
            if amount == None:
                amount = i['variety']
            name += " " +  amount
 
        productDetails = [name, i['brand'], i['price']['originalPrice'], i['price']['salePrice'], \
                i['size']['volumeSize'], None, 1, typee, i['sku']]
        if i['productTag'] != None:
            productDetails[-4] = i['productTag']['tagType'] 
 
        if productDetails[-4] == "Other": 
            title = i['productTag']['additionalTag']['name']
            if re.search("(...)\s[0-9]+\sfor\s\$[0-9]+(...)", title):
                splitter = title.split()
                productDetails[-3] = int(splitter[1])
                productDetails[3] = int(splitter[3][1:])/int(splitter[1])
                print("hi")
 
        if productDetails[-4] == 'IsMultiBuy' or productDetails[-4] == 'IsGreatPriceMultiBuy':
            productDetails[-3] = i['productTag']['multiBuy']['quantity']
            productDetails[3] = round(i['productTag']['multiBuy']['value'] / i['productTag']['multiBuy']['quantity'], 2)

        productList.append(tuple(productDetails))
    addToDatabase(productList, connection, tableName)
    maxPage = math.ceil(items / 120)
    print(url)
    
    if page < maxPage:
        page += 1
        editLocation = -15
        if page >= 11:
            editLocation = -16
        url = (url[: editLocation] + str(page) + '&target=browse')
        processData(connection, url, page, typee, tableName)


def main():
    tableName = datetime.today().strftime('%d/%m/%y')
    connection = databaseConnect()
    cursor = connection.cursor()
    createTable(cursor, tableName)
    locations = ["bakery", "deli-chilled-foods", "meat", "seafood", "baby-care", "baking-cooking", "biscuits-crackers", "breakfast-foods", "canned-prepared-foods", "chocolate-sweets-snacks", "cleaning-homecare", "drinks-hot-cold", "frozen-foods", "health-wellness", "home-kitchenware", "meal-ingredients", "office-entertainment", "personal-care", "pet-care", "liquor-beer-cider", "liquor-wine", "toys-party-needs"]
#    locations = ['chocolate-sweets-snacks']
    for iii in locations:
        page = 1
        url = 'https://shop.countdown.co.nz/api/v1/products/search?dasFilter=Department%3B%3B' + iii + '%3Bfalse&nextUI=true&size=120&page=1&target=browse'
        processData(connection, url, page, iii, tableName)
main()
















locations = ["christmas", "bakery", "deli-chilled-foods", "meat", "seafood", "baby-care", "baking-cooking", "biscuits-crackers", "breakfast-foods", "canned-prepared-foods", "chocolate-sweets-snacks", "cleaning-homecare", "drinks-hot-cold", "frozen-foods", "health-wellness", "home-kitchenware", "meal-ingredients", "office-entertainment", "personal-care", "pet-care"]


















headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'authority': 'shop.countdown.co.nz', 'method': 'GET', 'scheme': 'https', 'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json', 'cookie': 'cw-sgbabtoe=5ed1fb895e08457a959bfea283f004a1; ai_user=Xr+iO|2019-11-24T08:08:09.775Z; _gcl_au=1.1.711282692.1574582890; _vwo_uuid_v2=DD44BEF2AEFBBB8A33CA735790235D3DD|ae6b2d640f2afb0b5fc02da15165c1c0; _ga=GA1.3.1002884010.1574582891; _vwo_uuid=DD44BEF2AEFBBB8A33CA735790235D3DD; gig_bootstrap_3_PWTq_MK-V930M4hDLpcL_qqUx224X_zPBEZ8yJeX45RHI-uKWYQC5QadqeRIfQKB=login; _fbp=fb.2.1574582890969.1964198752; _vwo_ds=3%3Aa_1%2Ct_0%3A0%241574582853%3A9.47216273%3A%3A%3A2_1%3A1; kampyle_userid=8656-b3d1-da98-89ac-a1f9-eb4f-6722-527b; cd_user_id=16e9c7436d74fc-0d7de31c50ff53-1528110c-1fa400-16e9c7436d8737; _hjid=43cd69d9-47be-48ca-974a-94bf4131afb8; ASP.NET_SessionId=vvwb00jr3fm2o2npi14rxtzd; cw-laie=821de8359141436586a91359ac1aad8c; __RequestVerificationToken=eBCmAQ_xgOdVfx9pCoRLBhRW4kEzvvSmbnzK6IQQupmZjYU497jhGdckwARy1a873qvRsrzSf956AT5xgZ_ONB3Bx6kTn_tF1crVY33gwtE1; _gid=GA1.3.1672741318.1575936298; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; kampyleUserSession=1575936299641; kampyleUserSessionsCount=3; AKA_A2=A; cw-arjshtsw=red515944a28e4c02b127e73074db5972ralfcbqyu; _vwo_sn=1357767%3A7%3Arec2.visualwebsiteoptimizer.com%3A7%3A1; ai_sessioncw-=DOSI1|1575940667279|1575940811405.265; kampyleSessionPageCounter=8', 'expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'pragma': 'no-cache', 'referer': 'https://shop.countdown.co.nz/shop/specials/baking-cooking?nextUI=true', 'request-id': '|1b7e7d3f9f5a446f89edf57e8bddd044.be8c385f3b00412d', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'x-requested-with': 'OnlineShopping.WebApp'}

