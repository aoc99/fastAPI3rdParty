# from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request, Form, UploadFile,File
# import numpy as np
from . import  models, schemas
from .services import ServiceRegDsn 
from sql_app.database_session import get_db
# from app.logger import TimedRoute
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
# # from fastapi import FastAPI, File, Form, UploadFile

router = APIRouter(
    prefix="/api/v1/dsn/registration",
    tags=["Registrasi Digital Signature Nasabah"],
    responses={404: {"description": "Not found"}}
)
ServiceRegDsn = ServiceRegDsn()

@router.post("/register")
async def registerDsn(request: Request, photoKtp: UploadFile = File(), photoSelfie: UploadFile = File(), payload: schemas.registrationDsn = Depends(), db: Session = Depends(get_db)):
    # if (photoKtp.content_type in
    #     ["image/png", "image/jpeg"] and photoSelfie.content_type in ["image/png","image/jpeg"]):
    #     if len(photoKtp.file.read()) > photoKtp.file._max_size or len(photoSelfie.file.read()) > photoKtp.file._max_size:
    #         raise HTTPException(
    #             status_code=413,
    #             detail="File size is too big. Limit is 1Mb"
    #         )
    return await ServiceRegDsn.registration(request,photoKtp, photoSelfie, payload, db)
    # else:
    #     raise HTTPException(status_code=400, detail="Invalid document type")

@router.post("/register-link")
async def registerLink(payload: schemas.registerlink = Depends(), Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await ServiceRegDsn.registerLink(payload, db)

@router.post("/register-check")
async def registerCheck(payload: schemas.registerCheck, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await ServiceRegDsn.registerCheck(payload, db)


