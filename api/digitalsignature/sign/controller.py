from hurry.filesize import size, alternative
from fastapi import APIRouter, Depends, HTTPException, Request
import numpy as np
from . import schemas
from .services import ServiceSign
from sql_app.database_session import get_db
from app.logger import TimedRoute
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
import os.path

router = APIRouter(
    prefix="/api/v1/dsn/sign",
    tags=["Signing Dokumen"],
    responses={404: {"description": "Not found"}}
)
ServiceSign = ServiceSign()

@router.post("/upload-dok")
async def UploadDokumen(payload: schemas.uploadDok = Depends(), Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    # if (dict(payload)['document'].content_type == "application/pdf"):
    #     if len(dict(payload)['document'].file.read()) > 1024 * 1024 * 100:
    #         raise HTTPException(
    #             status_code=413,
    #             detail="File size is too big. Limit is 1Mb"
    #         )
    return await ServiceSign.uploadDok(Authorize, payload, db)

@router.post("/signing")
async def SigningDok(payload: schemas.signing = Depends(), Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await ServiceSign.signing(Authorize, payload, db)

@router.post("/bulk-sign")
async def BulkSign(payload: schemas.bulksign, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await ServiceSign.signing(Authorize, payload, db)
   


