import requests
from bs4 import BeautifulSoup
import json


# Pushes request to Pak n Save API that retrieves the links to all the pages I want to scrape from on the website
def getUrlLinks(s):
    data = s.get('https://www.paknsaveonline.co.nz/CommonApi/Navigation/MegaMenu?v=2401&storeId=21ecaaed-0749-4492-985e-4bb7ba43d59c').json()
    overallSections = (data['NavigationList'][0]["Children"])
    links = []
    for section in overallSections:
        for innerSection in (section["Children"]):
            links.append(innerSection["URL"])
    return links

def runSections(s, links):
    base = 'https://www.paknsaveonline.co.nz'
    for link in links:
        soup = BeautifulSoup(s.get(base + link + "?page=1").content)
        maxPage = int(soup.findAll("a", {"class": "btn btn--tertiary btn--large fs-pagination__btn"})[-1].text)
        for page in range(1, maxPage + 1):
            url = base + link + "?pg=" + str(page)
            print(url)
            scrapeKeywords(s, url)



def scrapeKeywords(s, url):
    soup = BeautifulSoup(s.get(url).content)
    items = soup.findAll("div", {"class": "fs-product-card"})
    resultsList = []
    for iii in items:
        productDetailsDict = json.loads(iii.find("div", {"class": "js-product-card-footer fs-product-card__footer-container"})['data-options'])
        productOutput = [iii.find("p", {"class": "u-color-half-dark-grey u-p3"}).text]
        productOutput += [(productDetailsDict['productId']), productDetailsDict['productName']]
        productOutput.append(productDetailsDict['ProductDetails']['PriceMode'])
        productOutput.append(productDetailsDict['ProductDetails']['PricePerItem'])
        resultsList.append(productOutput)
    print(len(resultsList))


def run():
    s = requests.Session()
    # scrapeKeywords(s, 'https://www.paknsaveonline.co.nz/category/fresh-foods-and-bakery?pg=2')
    # return
    links = getUrlLinks(s)
    runSections(s, links)


run()
