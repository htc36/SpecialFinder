from bs4 import BeautifulSoup
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
    print(total)

    

