from api.customer.models import conString
from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
import json
import hashlib, datetime
from requests.structures import CaseInsensitiveDict
from app.utils import Token
from app.Urlmdlware import connections


class CobAccount:

    def getCobAccouunt(db: Session, dataReq: schemas.cobAcc, url, skip: int = 0, limit: int = 100):
        try:
            data = jsonable_encoder(db.query(conString).filter(
                conString.aliasName == str(url)[22:]).first())
            print(type(data['moduleCode']))
            MODULE_CODE = data['moduleCode']
            secretkey = data['secretKey']
            secretkey = hashlib.sha256(secretkey.encode('utf-8')
                                    ).hexdigest()
            CHANNELID = "MDW-DGLN-001"
            REQUEST_TIME = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            REF_NO = "DIGILOAN-2022-10"
            tokenData = str(MODULE_CODE) + secretkey + REQUEST_TIME + REF_NO + CHANNELID
            token = hashlib.sha256(tokenData.encode('utf-8')).hexdigest()
            con = data['url']
            # print(con)
            params = {
                "AUTH_TOKEN": token,
                "REF_NO": REF_NO,
                "REQUEST_TIME": REQUEST_TIME,
                "MODULE_CODE": MODULE_CODE,
                "CHANNEL_ID": CHANNELID,
                "CIF": dataReq.CIF,
                "ACC_CCY": dataReq.ACC_CCY,
                "ACC_TYPE": dataReq.ACC_TYPE,
                "ACC_BRCH": dataReq.ACC_BRCH,
                "ACC_JOIN": dataReq.ACC_JOIN,
                "CUS_SHRT_NAME": dataReq.CUS_SHRT_NAME
            }
            sendData = requests.post(con, data=json.dumps(params))
            response = json.loads(sendData.text)
            return response
        except Exception as ex:
            return str(ex)
