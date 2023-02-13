from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class twitterScrapeModel(BaseModel):
    longitude: Union[str, None] = ''
    latitude: Union[str, None] = ''
    radius: Union[str, None] = ''
    konten: Union[str, None] = ''
