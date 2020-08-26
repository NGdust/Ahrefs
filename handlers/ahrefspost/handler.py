import json
import os

import couchdb
import requests
from couchdb import PreconditionFailed

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse




def handle(event):
    dbURL = f"http://{os.getenv('COUCHDB_USER')}:{os.getenv('COUCHDB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
    couch = couchdb.Server(dbURL)
    try:
        db = couch.create('href')
    except PreconditionFailed:
        db = couch['href']

    try:
        query = os.environ['Http_Query']
    except KeyError:
        return {"error": "No parameters found in the link"}
    path = urlparse(query).path.split('&')

    params = {}
    for item in path:
        key = item.split('=')[0]
        value = item.split('=')[1]
        params[key] = value

    try:
        responce = requests.get(f"https://apiv2.ahrefs.com?from=backlinks&"
                                f"target={params['domain']}&"
                                f"mode=domain&"
                                f"limit=2&"
                                f"order_by=ahrefs_rank%3Adesc&"
                                f"output=json&"
                                f"token={params['token']}")
        for item in json.loads(responce.text)['refpages']:
            db.save(item)
        return json.loads(responce.text)
    except Exception as error:
        return {"error": error}
