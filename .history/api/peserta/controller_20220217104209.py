from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header
from . import  models, schemas
from .services import Peserta as servicePeserta
from sql_app.database_session import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Peserta",
    tags=["Inquiry Peserta"],
    responses={404: {"description": "Not found"}},
)

@router.post("/Inquiry")
async def inquiry_peserta(peserta:schemas.PesertaBase, db: Session = Depends(get_db)):
    return servicePeserta.getPeserta(db, peserta)

@router.post("/verifikasiPertama")
async def verifikasiP_peserta( peserta:schemas.VerifikasiBase,db: Session = Depends(get_db)):
    return servicePeserta.verifikasiPeserta(db, peserta)

@router.post("/verifikasiFinal")
async def verifikasiF_peserta(peserta:schemas.VerifikasiBase,db: Session = Depends(get_db)):
    return servicePeserta.verifikasiFPeserta(db, peserta)


