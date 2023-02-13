from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import datetime, json, uuid

class PesertaBase(BaseModel):
    cabang: str
    kodeMitra: str
    namaOperator: str
    peserta: dict

class VerifikasiBase(BaseModel):
    kodeMitra: str
    cabang: str
    namaOperator: str
    jumlah: int
    peserta: list[dict] = []

