# from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request
import numpy as np
from . import  models, schemas
from .services import ServiceCustomer as serviceCust
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
async def ValidatePasscode(self, request: Request,dataReq:schemas.checkCust, db: Session = Depends(get_db)):
    return serviceCust.checkpasscode(db, self, dataReq, request)


