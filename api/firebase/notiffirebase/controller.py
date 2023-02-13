# from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, Request
import numpy as np
from . import  models, schemas
from .services import ServicenotifFirebase
from sql_app.database_session import get_db
from app.logger import TimedRoute
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

router = APIRouter(
    prefix="/api/v1/notif",
    tags=["Token Firebase"],
    responses={404: {"description": "Not found"}},
    route_class=TimedRoute
)
serviceFirebase = ServicenotifFirebase()

@router.post("/Firebase")
async def notifFirebase(request: Request, payload: schemas.checkCust, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await serviceFirebase.notif(request, Authorize, payload, db )

@router.post("/PushFirebase")
async def notifFirebase(request: Request, payload: schemas.pushNotif, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await serviceFirebase.Pushnotif(payload, db )


