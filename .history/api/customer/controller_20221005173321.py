from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request
import numpy as np
from . import  models, schemas
from .services import CobAccount as serviceCob
from sql_app.database_session import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Middleware",
    tags=["service Middleware"],
    responses={404: {"description": "Not found"}},
)

@router.post("/cobAccount")
async def cobAccount(request: Request,dataReq:schemas.cobAcc, db: Session = Depends(get_db)):
    return serviceCob.getCobAccouunt(db, dataReq, request.url)


