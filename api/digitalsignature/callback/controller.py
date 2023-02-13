import os.path
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from app.logger import TimedRoute
from sql_app.database_session import get_db
from .services import ServiceCallback
from . import schemas
import numpy as np
from fastapi import APIRouter, Depends, HTTPException, Request

router = APIRouter(
    prefix="/api/v1/dsn/callback",
    tags=["Callback"],
    responses={404: {"description": "Not found"}}
)
ServiceCallback = ServiceCallback()


@router.post("/regis")
async def UploadDokumen(payload: schemas.callback, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await ServiceCallback.regis(Authorize, payload, db) 
