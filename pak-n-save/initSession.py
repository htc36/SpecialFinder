import requests
import datetime
import json

def setUpSession(s, storeId):
    s.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
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
        if (raw[index][-2]) != "," and raw[index][-2] != "{":
            value.append([index, index+2])#, [''.join(raw[index: index+2])]))
    for indexs in value:
        raw[indexs[0]: indexs[1]] = [''.join(raw[indexs[0]: indexs[1]])]
    result = '\n'.join(raw)
    return json.loads(result)
def getStores():
    date = ((datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)).strftime("%d/%m/%y"))
    #data = json.loads(requests.get('https://www.paknsaveonline.co.nz/CommonApi/Store/GetStoreList').content)
    stores = [['Albany', '65defcf2-bc15-490e-a84f-1f13b769cd22'], ['Taupo', 'b92cc33f-b5a8-4b57-9b82-412946800020']]
    stores += [['Petone', '98ec3885-ac93-4fcb-807b-59c9055c52c4'], ['Whangarei', '529d66cc-60e3-432e-b8d1-efc9f2ec4919']]
    stores += [['Royal Oak', 'e1925ea7-01bc-4358-ae7c-c6502da5ab12']]
    return stores
# getStores()



