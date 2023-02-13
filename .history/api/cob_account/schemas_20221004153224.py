from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class cobAcc(BaseModel):
    REF_NO: int
    CHANNEL_ID: str
    MODULE_CODE: int
    REQUEST_TIME: int
    CIF: str
    ACC_CCY: str
    ACC_TYPE: str
    ACC_BRCH: int
    ACC_JOIN: bool
    CUS_SHRT_NAME: str