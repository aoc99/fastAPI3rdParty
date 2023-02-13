from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class twitterScrapeModel(BaseModel):
    longitude: str
    latitude: str
    radius: str
    konten: str
