# from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request
import numpy as np
from . import  models, schemas
from .services import ServiceCustomer 
from sql_app.database_session import get_db
from app.logger import TimedRoute
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

router = APIRouter(
    prefix="/customer",
    tags=["Get Token"],
    responses={404: {"description": "Not found"}},
    route_class=TimedRoute
)
serviceCust = ServiceCustomer()

@router.post("/checkpasscode")
async def ValidatePasscode(request: Request, payload: schemas.checkCust, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await serviceCust.checkpasscode(request, Authorize, payload, db )

@router.post("/tongdun")
async def ValidatePasscode(db: Session = Depends(get_db)):
    return await serviceCust.Tongdun(db)


