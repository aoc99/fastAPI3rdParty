from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class cobAcc(BaseModel):
    CHANNEL_ID: Union[str, None] = ''
    MODULE_CODE: Union[str, None] = ''
    REQUEST_TIME: Union[str, None] = ''
    CIF: Union[str, None] = ''
    ACC_CCY: Union[str, None] = ''
    ACC_TYPE: Union[str, None] = ''
    ACC_BRCH: Union[str, None] = ''
    ACC_JOIN: Union[str, None] = ''
    CUS_SHRT_NAME: Union[str, None] = ''