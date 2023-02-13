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


class CommonQueryParams:
    def __init__(self, request: Request, dataReq: schemas.checkCust, db: Session = Depends(get_db)):
        self.request = request
        self.dataReq = dataReq
        self.session = db

@router.post("/checkpasscode")
async def ValidatePasscode(dataCommon: CommonQueryParams = Depends()):
    return serviceCust.checkpasscode(dataCommon)


