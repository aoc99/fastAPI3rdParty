import snscrape.modules.twitter as twitScrape
import snscrape.modules.instagram as instaScrape
import json
import os
import logging
import datetime
import itertools
import pandas as pd
from python_elastic_logstash import ElasticHandler, ElasticFormatter
from elasticsearch import Elasticsearch
from app.mappingTwit import tweet_body
import numpy as np
from email import header
from urllib import request
from sqlalchemy import false
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi.encoders import jsonable_encoder
import requests, json
from requests.structures import CaseInsensitiveDict


class twitterScrapeService:

    def twitterbyLonglat(db: Session, peserta: schemas.twitterScrapeModel, skip: int = 0, limit: int = 100):
        try:
            es_client = Elasticsearch("http://10.6.226.246:9200")
            loc = "-6.93653, 107.61315, 1km"
            # loc = peserta.longitude+peserta.latitude+peserta.radius
            scraper = pd.DataFrame(itertools.islice(twitScrape.TwitterSearchScraper(
                'geocode:"{}"'.format(loc)).get_items(), 1)).replace({np.nan: None})
            print(loc)
            print(scraper.to_json)
            return scraper
            # logging.info(
            #     f"Creating index {'tweet-log'} with the following schema:{json.dumps(tweet_body, indent=2)}")
            # es_client.indices.create(index='tweet-log', ignore=400, body=tweet_body)
            # logging.info(
            #     f"Writing {len(scraper.index)} documents to ES index {'tweet-log'}")
            # for doc in scraper.apply(lambda x: x.to_dict(), axis=1):
            #     a = {list(doc.keys())[list(doc.values()).index(
            #         doc['date'])]: doc['date'].isoformat()}
            #     doc.update(a)
            #     print(json.dumps(doc, default=str))
            #     es_client.index(index='tweet-log',
            #                     body=json.dumps(doc, default=str))


            # LOG_HANDLER.info("{}".format(analytics))
            # df_city = pd.DataFrame(itertools.islice(twitScrape.TwitterSearchScraper(
            #     'butuh uang near:"bandung" within:10km').get_items(), 10))[['date', 'content']]
            # print(df_city)

            # loc = '-6.93653, 107.61315, 10km'
            # scraper = pd.DataFrame(itertools.islice(instaScrape.InstagramLocationScraper(
            #     'butuh uang geocode:"{}"'.format(loc)).get_items(), 10))
            # print(scraper.to_json)
        except Exception as ex:
            return str(ex)
