import json
import os
import requests
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB')}")
DeclarativeBase = declarative_base()

class Href(DeclarativeBase):
    __tablename__ = 'href'

    id = Column(Integer, primary_key=True)
    url_to = Column('url_to', String)
    first_origin = Column('first_origin', String)
    last_origin = Column('last_origin', String)
    ugc = Column('ugc', String)
    sponsored = Column('sponsored', String)
    url_from = Column('url_from', String)
    ahrefs_rank = Column('ahrefs_rank', String)
    domain_rating = Column('domain_rating', String)
    ahrefs_top = Column('ahrefs_top', String)
    ip_from = Column('ip_from', String)
    links_internal = Column('links_internal', String)
    links_external = Column('links_external', String)
    page_size = Column('page_size', String)
    encoding = Column('encoding', String)
    language = Column('language', String)
    title = Column('title', String)
    first_seen = Column('first_seen', String)
    last_visited = Column('last_visited', String)
    prev_visited = Column('prev_visited', String)
    original = Column('original', String)
    link_type = Column('link_type', String)
    redirect = Column('redirect', String)
    nofollow = Column('nofollow', String)
    alt = Column('alt', String)
    anchor = Column('anchor', String)
    text_pre = Column('text_pre', String)
    text_post = Column('text_post', String)
    http_code = Column('http_code', String)
    url_from_first_seen = Column('url_from_first_seen', String)

    def __repr__(self):
        return "".format(self.url_to)


def handle(event):
    DeclarativeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

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
                                f"target={params['url']}&"
                                f"mode=domain&"
                                f"limit=2&"
                                f"order_by=ahrefs_rank%3Adesc&"
                                f"output=json&"
                                f"token={os.getenv('TOKEN_AHREFS')}")
        for item in json.loads(responce.text)['refpages']:
            session.add(Href(**item))
        session.commit()
        session.close()
        return json.loads(responce.text)
    except Exception as error:
        return {"error": error}