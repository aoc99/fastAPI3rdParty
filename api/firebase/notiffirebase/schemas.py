from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class checkCust(BaseModel):
    data: str

class pushNotif(BaseModel):
    to: str
    notification: dict