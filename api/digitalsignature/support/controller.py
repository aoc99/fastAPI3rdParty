# from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
import numpy as np
from . import  models, schemas
from .services import ServiceSupportDsn 
from sql_app.database_session import get_db
from app.logger import TimedRoute
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

router = APIRouter(
    prefix="/api/v1/dsn/support",
    tags=["Digital Signature Support"],
    responses={404: {"description": "Not found"}}
)
ServiceSupportDsn = ServiceSupportDsn()

@router.get("/ping")
async def TestCon(db: Session = Depends(get_db)):
    return await ServiceSupportDsn.tesCon(db)

@router.get("/province")
async def getProvince(db: Session = Depends(get_db)):
    return await ServiceSupportDsn.getProvince(db)

@router.get("/district")
async def getdistrict(idprovince: int,db: Session = Depends(get_db)):
    return await ServiceSupportDsn.getDistrict(idprovince,db)

@router.get("/subdistrict")
async def getsubdistrict(idprovince: int, iddistrict: int,db: Session = Depends(get_db)):
    return await ServiceSupportDsn.getSubdistrict(idprovince,iddistrict,db)

@router.get("/cekkuota")
async def getcekkuota(db: Session = Depends(get_db)):
    return await ServiceSupportDsn.getCekkuota(db)

