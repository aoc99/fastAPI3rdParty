from fastapi import APIRouter, Depends, HTTPException
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
async def cobAccount(dataReq:schemas.cobAcc, db: Session = Depends(get_db)):
    return await serviceCob.getCobAccouunt(db, dataReq)


