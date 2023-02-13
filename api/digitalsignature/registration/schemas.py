from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid, datetime
from fastapi import  UploadFile, File

class registrationDsn(BaseModel):
    email: str
    name: str
    gender: str
    dob: str
    pob: str
    nik: str
    mobile: str
    province: str
    district: str
    sub_district: str
    address: str
    zip_code: str

class registerlink(BaseModel):
    email: str

class registerCheck(BaseModel):
    nik: str
    action: str
    email: str
