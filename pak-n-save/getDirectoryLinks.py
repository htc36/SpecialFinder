import requests
from bs4 import BeautifulSoup
import json

s = requests.Session()

data = s.get('https://www.paknsaveonline.co.nz/CommonApi/Navigation/MegaMenu?v=2401&storeId=21ecaaed-0749-4492-985e-4bb7ba43d59c').json()
overallSections = (data['NavigationList'][0]["Children"])
links = []

for section in overallSections:
    for innerSection in (section["Children"]):
        links.append(innerSection["URL"])
