from sqlalchemy import false
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi.encoders import jsonable_encoder
import requests, json
from requests.structures import CaseInsensitiveDict
from app.utils import Token
from app.Urlmdlware import connections

class CobAccount:

    def getCobAccouunt(db: Session, dataReq: schemas.cobAcc, skip: int = 0, limit: int = 100):
        try:
            print(connections['custOnBoard'])
            requestData = jsonable_encoder(Token.getToken(db))
            con = connections['cobAccount']
            params = {
                "AUTH_TOKEN": requestData['AUTH_TOKEN'],
                "REF_NO": requestData['REF_NO'],
                "REQUEST_TIME": requestData['REQUEST_TIME'],
                "MODULE_CODE": requestData['MODULE_CODE'],
                "CHANNEL_ID": requestData['CHANNEL_ID'],
                "CIF": dataReq.CIF,
                "ACC_CCY": dataReq.ACC_CCY,
                "ACC_TYPE": dataReq.ACC_TYPE,
                "ACC_BRCH": dataReq.ACC_BRCH,
                "ACC_JOIN": dataReq.ACC_JOIN,
                "CUS_SHRT_NAME": dataReq.CUS_SHRT_NAME
            }
            # sendData = requests.post(con, data=json.dumps(params))
            # response = json.loads(sendData.text)
            # return response
        except Exception as ex:
            return str(ex)
