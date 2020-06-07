import requests
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


