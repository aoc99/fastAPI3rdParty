from fastapi import APIRouter, Depends, HTTPException
import snscrape.modules.twitter as twitScrape
import snscrape.modules.instagram as instaScrape
import json, os
import logging
import datetime
import itertools, pandas as pd
from python_elastic_logstash import ElasticHandler, ElasticFormatter
from elasticsearch import Elasticsearch
from mappingTwit import tweet_body
import numpy as np
from . import  models, schemas
from .services import twitterScrapeService as serviceTwitter
from sql_app.database_session import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Osint",
    tags=["Osint Social Media"],
    responses={404: {"description": "Not found"}},
)

@router.post("/Inquiry")
async def inquiry_peserta(peserta:schemas.twitterScrapeModel, db: Session = Depends(get_db)):
    return serviceTwitter.twitterbyLonglat(db, peserta)


