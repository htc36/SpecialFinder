import requests
import datetime
import json
from fake_useragent import UserAgent

def setUpSession(s, storeId):
    ua = UserAgent()
    s.headers = {'User-Agent': ua.random}
    s.get('https://www.paknsaveonline.co.nz/category/fresh-foods-and-bakery')
    s.post('https://www.paknsaveonline.co.nz/CommonApi/Store/ChangeStore?storeId=' + storeId).json()
    required_args = {
        'name': 'STORE_ID',
        'value': storeId + '|False'
    }
    optional_args = {
        'version': 0,
        'port': None,
        'domain': 'www.paknsaveonline.co.nz',
        'path': '/',
        'secure': False,
        'expires': None,
        'discard': True,
        'comment': None,
        'comment_url': None,
        'rest': {'HttpOnly': None},
        'rfc2109': False
    }
    my_cookie = requests.cookies.create_cookie(**required_args, **optional_args)
    s.cookies.set_cookie(my_cookie)
    return s
def fixJson(raw):
    value = []
    for index in range(0, len(raw) - 2):
        test = raw[index].split('"')
        if len(test) > 5:
            test[1] = '"' + test[1] + '"'
            test[3] = '"' + test[3]
            test[-2] = test[-2] + '"'
            raw[index] = ''.join(test)

        if (raw[index][-2]) != "," and raw[index][-2] != "{":
            value.append([index, index+2])#, [''.join(raw[index: index+2])]))
    for indexs in value:
        raw[indexs[0]: indexs[1]] = [''.join(raw[indexs[0]: indexs[1]])]
    result = '\n'.join(raw)
    return json.loads(result)
def getAllStores(s):
    ua = UserAgent()
    s.headers = {'User-Agent': ua.random}
    storeDict = s.post('https://www.paknsaveonline.co.nz/CommonApi/Store/GetStoreList').json()['stores']
    fullStoreDictonary = {}
    for storeObject in storeDict:
        fullStoreDictonary[storeObject['name']] = storeObject
    return(fullStoreDictonary)



def getStores():
    date = ((datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)).strftime("%d/%m/%y"))
    #data = json.loads(requests.get('https://www.paknsaveonline.co.nz/CommonApi/Store/GetStoreList').content)
    stores = [['Albany', '65defcf2-bc15-490e-a84f-1f13b769cd22'], ['Taupo', 'b92cc33f-b5a8-4b57-9b82-412946800020']]
    stores += [['Petone', '98ec3885-ac93-4fcb-807b-59c9055c52c4'], ['Whangarei', '529d66cc-60e3-432e-b8d1-efc9f2ec4919']]
    stores += [['Royal Oak', 'e1925ea7-01bc-4358-ae7c-c6502da5ab12']]
    return stores
# getStores()



