from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class twitterScrapeModel(BaseModel):
    longitude: Union[str, None] = None
    latitude: Union[str, None] = None
    radius: Union[str, None] = None
    konten: Union[str, None] = None
