from fastapi import APIRouter, Depends, HTTPException
import numpy as np
from . import  models, schemas
from .services import twitterScrapeService as serviceTwitter
from sql_app.database_session import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Osint",
    tags=["Osint Social Media"],
    responses={404: {"description": "Not found"}},
)

@router.post("/twitter")
async def OsinTwitter(peserta:schemas.twitterScrapeModel, db: Session = Depends(get_db)):
    return serviceTwitter.twitterbyLonglat(db, peserta)


