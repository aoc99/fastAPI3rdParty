from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class cobAcc(BaseModel):
    REF_NO: str
    CHANNEL_ID: str
    MODULE_CODE: str
    REQUEST_TIME: str
    CIF: str
    ACC_CCY: str
    ACC_TYPE: str
    ACC_BRCH: str
    ACC_JOIN: str
    CUS_SHRT_NAME: str