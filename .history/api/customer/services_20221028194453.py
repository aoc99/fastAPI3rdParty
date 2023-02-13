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
from fastapi_jwt_auth import AuthJWT


class ServiceCustomer:

    def __init__(self):
        self.token = Tokenizer()
        
    async def checkpasscode(self, request, Authorize,payload, db):
        try:
            key_args = request.query_params['key']
            if key_args:
                if self.token.checkClientId(key_args):
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
                                return HTTPResponse.not_acceptable()
                            db.session.commit()
                        else:
                            db.query(Customer).filter(
                                Customer._id == customer._id).update({"useBiometric": False})
                            db.session.commit()
                            return HTTPResponse.validation_error(
                                "Akun Anda Ditangguhkan, Silahkan menggunakan fitur Lupa PIN")
                    else:
                        return HTTPResponse.not_found("Nasabah tidak terdaftar")
                else:
                    return HTTPResponse.unauthorized("Unknown Client")
            else:
                return HTTPResponse.forbidden("Tidak ada Key Otorisasi")
        except Exception as err:
            db.rollback()
            return HTTPResponse.server_error(err)
        finally:
            db.close()
