import datetime
from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
from fastapi import Request, Depends
from sql_app.database_session import get_db
import json
import bcrypt
import hashlib, datetime, requests
from requests.structures import CaseInsensitiveDict
from app.tokenizer import Tokenizer
from app.responses import HTTPResponse 
from fastapi.responses import JSONResponse
from app.config import Config

class ServiceSupportDsn:

    def __init__(self):
        self.response = HTTPResponse()
        self.token = Tokenizer()
        self.apikey = Config.APIKEY
        
    async def tesCon(self,db: Session = Depends(get_db)):
        try:
            payload={}
            files={}
            headers = {
            # 'Accept': 'multipart/form-data',
            # 'Content-Type': 'application/json',
            'apikey': self.apikey
            }
            req = requests.get(
                'http://10.6.226.246:25117/api/v1/dsn/support/ping', headers=headers)
            response = json.loads(req.text)
            return JSONResponse(response)
        except Exception as err:
            return self.response.server_error(str(err))
        finally:
            req.connection.close()
    
    async def getProvince(self,db: Session = Depends(get_db)):
        try:
            payload={}
            files={}
            headers = {
            'apikey': self.apikey
            }
            req = requests.get('https://apix.sandbox-111094.com/v2/data/province', headers=headers)
            response = json.loads(req.text)
            return JSONResponse(response)
        except Exception as err:
            return self.response.server_error(str(err))
        finally:
            req.connection.close()

    async def getDistrict(self, id, db):
        try:
            headers = {
            'apikey': self.apikey
            }
            req = requests.get(
                'http://10.6.226.246:25117/api/v1/dsn/support/district?idprovince='+str(id), headers=headers)
            response = json.loads(req.text)
            return JSONResponse(response)
        except Exception as err:
            return self.response.server_error(str(err))
        finally:
            req.connection.close()

    async def getSubdistrict(self,idprovince,iddistrict,db: Session = Depends(get_db)):
        try:
            headers = {
            'apikey': self.apikey
            }
            req = requests.get('https://apix.sandbox-111094.com/v2/data/subdistrict?province='+str(idprovince)+'&district='+str(iddistrict), headers=headers)
            response = json.loads(req.text)
            return JSONResponse(response)
        except Exception as err:
            return self.response.server_error(str(err))
        finally:
            req.connection.close()

    async def getCekkuota(self,db: Session = Depends(get_db)):
        try:
            headers = {
                'Content-Type': "multipart/form-data",
                'apikey': self.apikey
            }
            req = requests.get('https://apix.sandbox-111094.com/v2/tool/check-quota', headers=headers)
            response = json.loads(req.text)
            return JSONResponse(response)
        except Exception as err:
            return self.response.server_error(str(err))
        finally:
            req.connection.close()
