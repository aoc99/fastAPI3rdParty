from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid


class callback(BaseModel):
    status: str
    code: str
    timestamp: str
    message: str
    data: dict