from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request
import numpy as np
from . import  models, schemas
from .services import CobAccount as serviceCob
from sql_app.database_session import get_db
from app.logger import TimedRoute
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/customer",
    tags=["Get Token"],
    responses={404: {"description": "Not found"}},
    route_class=TimedRoute
)

@router.post("/checkpasscode")
async def ValidatePasscode(request: Request,dataReq:schemas.cobAcc, db: Session = Depends(get_db)):
    return serviceCob.getCobAccouunt(db, dataReq, request.url)

@router.post("/cob")
async def cob(request: Request,dataReq:schemas.cob, db: Session = Depends(get_db)):
    return serviceCob.getCob(db, dataReq, request.url)


