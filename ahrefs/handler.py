import os
import requests
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


def checkAhrefs(token, domain):
    responce = requests.get(f"https://apiv2.ahrefs.com?token={token}&target=ahrefs.com&limit=1000&output=json&from=ahrefs_rank&mode={domain}")
    return responce.text

def generateParams(path):
    params = {}
    for item in path:
        key = item.split('=')[0]
        value = item.split('=')[1]
        params[key] = value
    return params

def handle(req):
    query = os.environ['Http_Query']
    path = urlparse(query).path.split('&')
    params = generateParams(path)
    try:
        return checkAhrefs(params['token'], params['domain'])
    except KeyError as error:
        return {"error": error}
