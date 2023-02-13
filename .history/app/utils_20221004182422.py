import hmac
import datetime
import requests
import json
import hashlib
from sql_app.database_session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

class Token:
    async def getToken(db: Session = Depends(get_db)):
        MODULE_CODE = "710002"
        secretkey = "testsit"
        secretkey = hashlib.sha256(secretkey.encode('utf-8')
                                ).hexdigest()
        CHANNELID = "MDW-DGLN-001"
        REQUEST_TIME = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        REF_NO = "DIGILOAN-2022-10"
        tokenData = MODULE_CODE + secretkey + REQUEST_TIME + REF_NO + CHANNELID
        # print(tokenData)
        token = hashlib.sha256(tokenData.encode('utf-8')).hexdigest()
        data = {}
        data = data.append(MODULE_CODE)
        return data
