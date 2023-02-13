import datetime
from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
from fastapi import Request, Depends
from sql_app.database_session import get_db
import json
import bcrypt
import hashlib, datetime
from requests.structures import CaseInsensitiveDict
from app.tokenizer import Tokenizer 
# from api.digitalsignature.upload.models import Customer
from app.responses import HTTPResponse 
from fastapi.responses import JSONResponse


class ServiceCallback:

    def __init__(self):
        self.response = HTTPResponse()
        self.token = Tokenizer()
        
    async def regis(self, Authorize, payload, db: Session = Depends(get_db)):
        try:
            headers = {
                'Accept': 'application/json',
            }
            payload = payload.dict()
            print(json.dumps(payload))
            req = requests.post('http://10.6.226.247:6111/api/konsumer/v1/callback/document', headers=headers,
                                data=json.dumps(payload))
            resp = json.loads(req.text)
            return resp
        except Exception as err:
            return self.response.server_error(str(err))
