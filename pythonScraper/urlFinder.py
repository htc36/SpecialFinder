from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

def departmentFinder():
    url = 'https://shop.countdown.co.nz'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    browseBanner = soup.find('div', {"id": "BrowseSlideBox"})
    elements = (browseBanner.find_all('li', class_ = 'toolbar-slidebox-item'))
    listOfDepartments = []
    for iii in elements:
        listOfDepartments.append(iii.a.get('href').split('/')[-1])
    return listOfDepartments

def productCounter():
    departments = departmentFinder()
    total = 0
    for iii in departments:
        time.sleep(random.uniform(3,7))
        url = 'https://shop.countdown.co.nz/shop/browse/' + iii
        url = 'https://shop.countdown.co.nz/shop/browse/easter'
        print(url)
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            elements = (soup.find('div', class_ = 'paging-description hidden-tablet hidden'))
        except:
            elements = (soup.find('div', class_ = 'https://shop.countdown.co.nz/shop/browse/easter'))
        print(elements)

        amount = int(elements.text.split()[0])
        print(amount)
        total += amount

def locationFinder():
    url = 'https://shop.countdown.co.nz'
    s = requests.Session()
    response = s.get(url)
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'method': 'GET', 'accept-encoding': 'gzip, deflate, br', 'cache-control': 'no-cache', 'content-type': 'application/json', 'pragma': 'no-cache', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'x-requested-with': 'OnlineShopping.WebApp'}

    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.find("a", {"class": "shop-info-action show-delivery-address-link "}).contents

    print(mydivs)
    #r = s.post('https://shop.countdown.co.nz/shop/setsuburb?_mode=ajax&_ajaxsource=shop-info-panel&_referrer=%2F&_bannerViews=&_showTrolley=false', data = {
    r = s.post('https://shop.countdown.co.nz/shop', data = {
    "PostcodeSuburb" : "Riccarton,+Christchurch+Hornby",
    "postcodeSuburb-validated" : "Glenfield",
    "SuburbID": "481",
    "__RequestVerificationToken": "o6jnIzX3Pf62JtBBynMmB5Nqrxf2Rzkz0a3ZjOjbElhyhkmivsUQTmhw17_6VnlMSM1neBTRt8LIbjaxhHy0KiqmzaPH52Ul2KOGHOsc7JQ1"
    }, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)
    mydivs = soup.find("a", {"class": "shop-info-action show-delivery-address-link "}).contents
    print(soup)

#locationFinder()





    

