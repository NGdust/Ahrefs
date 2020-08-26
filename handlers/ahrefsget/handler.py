import json
import os
import pymongo
import requests
import couchdb
from couchdb import PreconditionFailed

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse



def handle(event):
    try:
        dbURL = f"http://{os.getenv('COUCHDB_USER')}:{os.getenv('COUCHDB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
        couch = couchdb.Server(dbURL)
        try:
            db = couch['href']
        except Exception as error:
            return {"error": error}

        responce = []
        for i in db:
            responce.append({
                "url_to": db[i]['url_to'],
                "url_from": db[i]['url_from'],
                "ahrefs_rank": db[i]['ahrefs_rank'],
                "domain_rating": db[i]['domain_rating'],
                "ahrefs_top": db[i]['ahrefs_top'],
                "ip_from": db[i]['ip_from'],
                "links_internal": db[i]['links_internal'],
                "links_external": db[i]['links_external'],
                "page_size": db[i]['page_size'],
                "encoding": db[i]['encoding'],
                "language": db[i]['language'],
                "title": db[i]['title'],
                "first_seen": db[i]['first_seen'],
                "last_visited": db[i]['last_visited'],
                "prev_visited": db[i]['prev_visited'],
                "original": db[i]['original'],
                "link_type": db[i]['link_type'],
                "redirect": db[i]['redirect'],
                "nofollow": db[i]['nofollow'],
                "alt": db[i]['alt'],
                "anchor": db[i]['anchor'],
                "text_pre": db[i]['text_pre'],
                "text_post": db[i]['text_post'],
                "http_code": db[i]['http_code'],
                "url_from_first_seen": db[i]['url_from_first_seen'],
            })
        return {"refpages": json.dumps(responce)}
    except Exception as error:
        return {"error": error}
