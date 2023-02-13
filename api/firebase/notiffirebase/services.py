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
from api.firebase.notiffirebase.models import Customer
from app.responses import HTTPResponse 
from fastapi.responses import JSONResponse


class ServicenotifFirebase:

    def __init__(self):
        self.response = HTTPResponse()
        self.token = Tokenizer()
        
    async def notif(self, request, Authorize,payload, db: Session = Depends(get_db)):
        try:
            key_args = request.query_params
            if key_args:
                if self.token.checkClientId(key_args['key']):
                    data = json.loads(self.token.decrypt(payload.dict()['data']))
                    phoneNumber = data["phoneNumber"]
                    firebaseToken = data["firebaseToken"]
                    customer = db.query(Customer).filter(
                        Customer.phoneNumber == phoneNumber, Customer.isDeleted == False).first()
                    if customer:
                        db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
                            {"firebaseToken": firebaseToken})
                        customer = self.token.createCustomerObject(db,
                            customerId=customer._id)
                        db.commit()
                        return self.response.accepted("Token berhasil disimpan")
                    else:
                        return self.response.not_found("Nasabah tidak terdaftar")
                else:
                    return self.response.unauthorized("Unknown Client")
            else:
                return self.response.forbidden("Tidak ada Key Otorisasi")
        except Exception as err:
            db.rollback()
            return self.response.server_error(str(err))
        finally:
            db.close()

    async def Pushnotif(self, payload,db):
        try:
            headers={
                'Content-Type':'application/json',
                'Authorization': 'Bearer AAAAwz0xEaY:APA91bESerHojgvp-Aw7lsQ9avitcMDC9ScBi76o6CgCEBXQewL7wVPm7GgvSjmvTI9SnJ9ntBgSmEdnblTWD3DP-VKSOZImIr7-yn1tAM_Kg4NXLmjzMr2TeKaptgZrzlrLu8kkmBkW'}
            req = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers,data=json.dumps(dict(payload)), proxies={'http':'http://10.12.14.2:80'})
            return json.loads(req.text)
        except Exception as err:
            return self.response.server_error(str(err))