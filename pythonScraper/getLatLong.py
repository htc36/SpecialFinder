import requests
from fake_useragent import UserAgent
from databaseCommands import *
import json


def createSession():
    ua = UserAgent()
    s = requests.Session()
    headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'method': 'GET', 'accept-encoding': 'gzip, deflate, br', 'cache-control': 'no-cache', 'content-type': 'application/json', 'pragma': 'no-cache', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': ua.random, 'x-requested-with': 'OnlineShopping.WebApp'}
    s.headers = headers
    return s
connection = databaseConnect()
s = createSession()
data = s.get('https://www.countdown.co.nz/api/stores/?includeStoresEligibleForMyCd=true').json()
allStoreDict = {}
for iii in data:
    if iii['Brand'] == 'Countdown':
        allStoreDict[iii['Brand'] + " " + iii["Name"]] = iii

cursor = connection.cursor()
query = "SELECT * from countdownStores"
cursor.execute(query)
rows = cursor.fetchall()
result = []
print(rows)
for iii in rows:
    if iii[1] in allStoreDict.keys():
        matchedStore = (allStoreDict[iii[1]])
    elif iii[1].split(" ")[-1] == "St":
        key = iii[1].split(' ')[0 : -1] + ["Street"]
        matchedStore = allStoreDict[' '.join(key)]
    result.append([str(matchedStore["Location"]["Latitude"]), str(matchedStore["Location"]["Longitude"]), matchedStore["ContactDetails"], matchedStore["OpeningHours"], iii[0]])

print(result)
query = "UPDATE `countdownStores` set lat = %s, lng = %s, contactDetails = %s, openingHours = %s WHERE storeCode = %s"
cursor.executemany(query, result)
connection.commit()
print("added To database")
cursor.close()


