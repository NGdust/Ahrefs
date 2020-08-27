import json
import os

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
    try:
        DeclarativeBase.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        responce = []
        for item in session.query(Href):
            responce.append({
                "url_to": item.url_to,
                "url_from": item.url_from,
                "ahrefs_rank": item.ahrefs_rank,
                "domain_rating": item.domain_rating,
                "ahrefs_top": item.ahrefs_top,
                "ip_from": item.ip_from,
                "links_internal": item.links_internal,
                "links_external": item.links_external,
                "page_size": item.page_size,
                "encoding": item.encoding,
                "language": item.language,
                "title": item.title,
                "first_seen": item.first_seen,
                "last_visited": item.last_visited,
                "prev_visited": item.prev_visited,
                "original": item.original,
                "link_type": item.link_type,
                "redirect": item.redirect,
                "nofollow": item.nofollow,
                "alt": item.alt,
                "anchor": item.anchor,
                "text_pre": item.text_pre,
                "text_post": item.text_post,
                "http_code": item.http_code,
                "url_from_first_seen": item.url_from_first_seen,
            })
        session.close()
        return {"refpages": json.dumps(responce)}
    except Exception as error:
        return {"error": error}
