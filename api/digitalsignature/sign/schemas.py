from typing import List, Optional, Union
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid
from fastapi import UploadFile, File


class uploadDok(BaseModel):
    document: UploadFile = File()
    signature:  Optional[str]
    ematerai: Optional[str]
    document_password: str 
    is_in_order: str
    expiration_date: str
    show_qrcode: str
    qrcode_position: str
    qrcode_page: str
    page_number: str
    qrcode_size: str

class signing(BaseModel):
    document_id: str
    user_email: str

class bulksign(BaseModel):
    document_id: List[str]