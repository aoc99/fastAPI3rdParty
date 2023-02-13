import datetime
from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
from fastapi import Request
import json
import bcrypt
import hashlib, datetime
from requests.structures import CaseInsensitiveDict
from app.tokenizer import Tokenizer 
from api.customer.models import Customer
from app.responses import HTTPResponse 
from fastapi.responses import JSONResponse


class ServiceCustomer:

    def __init__(self):
        self.response = HTTPResponse()
        self.token = Tokenizer()
        
    async def checkpasscode(self, request, Authorize,payload, db):
        try:
            key_args = request.query_params
            if key_args:
                if self.token.checkClientId(key_args['key']):
                    data = json.loads(self.token.decrypt(payload.dict()['data']))
                    print(data)
                    passcode = data["passcode"]
                    phoneNumber = data["phoneNumber"]
                    customer = db.query(Customer).filter(
                        Customer.phoneNumber == phoneNumber, Customer.isDeleted == False).first()
                    if customer:
                        if customer.failedPasscode < 3:
                            isMatched = bcrypt.checkpw(
                                str(passcode).encode("utf8"), customer.passcode.encode("utf8"))
                            if isMatched:
                                db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
                                    {"failedPasscode": 0})
                                customer = self.token.createCustomerObject(db,
                                    customerId=customer._id)
                                DATA = {
                                    "access_token": self.token.createToken(Authorize,customer),
                                    "token_type": "bearer",
                                    "data": self.token.encrypt(customer)
                                }
                                return JSONResponse(DATA)
                            else:
                                db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
                                    {"failedPasscode": customer.failedPasscode + 1})
                                DATA = {"access_token": None,
                                             "token_type": None, "data": {}}
                                db.session.commit()
                                return self.response.not_acceptable()
                        else:
                            db.query(Customer).filter(
                                Customer._id == customer._id).update({"useBiometric": False})
                            db.session.commit()
                            return self.response.validation_error(
                                "Akun Anda Ditangguhkan, Silahkan menggunakan fitur Lupa PIN")
                    else:
                        return self.response.not_found("Nasabah tidak terdaftar")
                else:
                    return self.response.unauthorized("Unknown Client")
            else:
                return self.response.forbidden("Tidak ada Key Otorisasi")
        except Exception as err:
            db.rollback()
            return self.response.server_error(str(err))
        # finally:
        #     db.close()

    async def Tongdun(db):
        
        url = f"http://api.tongdun.net/Carpo/query/v1?partner_code=BJB_id&partner_key=b95c3326ed974e9bacb9062c006283ee"
        header = {"Content-Type": "application/json"}
        body = {
            "id_num": "3204090709890004",
            "act_mbl": "085603179405",
            "full_nm": "Gaga",
            "app_name": "BJB_and",
            "package_id": "CarpoIDBJBScore001",
            "task_id": "",
            "apply_time": "31-10-2022"
        }
        print(body)
        http = requests.post(url, data=json.dumps(body), headers=header)
        res = json.loads(http.text)
        print(res)
        return res
