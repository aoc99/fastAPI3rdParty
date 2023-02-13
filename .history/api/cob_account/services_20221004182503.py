from sqlalchemy import false
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi.encoders import jsonable_encoder
import requests, json
from requests.structures import CaseInsensitiveDict
from app.utils import Token

class CobAccount:

    def getCobAccouunt(db: Session, dataReq: schemas.cobAcc, skip: int = 0, limit: int = 100):
        try:
            print(Token.getToken(db))
            # con = 'http://10.6.226.79:12747/mdw/basic/infcus'
            # params = {
            #     "AUTH_TOKEN": Token.getToken,
            #     "REF_NO": Token.getToken.REF_NO,
            #     "REQUEST_TIME": REQUEST_TIME,
            #     "MODULE_CODE": MODULE_CODE,
            #     "CHANNEL_ID": CHANNELID,
            #     "CIF": "1688Z6"
            # }
            # sendData = requests.post(con, data=json.dumps(params))
            # response = json.loads(sendData.text)
            # print(response)
        except Exception as ex:
            return str(ex)
