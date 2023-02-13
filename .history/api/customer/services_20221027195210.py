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
        self.token = Tokenizer()
        
    async def checkpasscode(self, request, payload, db):
        # try:
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
                            print(isMatched)
                            if isMatched:
                                db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
                                    {"failedPasscode": 0})
                                customer = self.token.createCustomerObject(db,
                                    customerId=customer._id)
                                DATA = {
                                    "access_token": self.token.createToken(customer),
                                    "token_type": "bearer",
                                    "data": self.token.encrypt(customer)
                                }
                                print(DATA)
                                # return JSONResponse(DATA)
                            # else:
                            #     db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
                            #         {"failedPasscode": customer.failedPasscode + 1})
                            #     DATA = {"access_token": None,
                            #                  "token_type": None, "data": {}}
                            #     HTTP_CODE = 406
                            # db.session.commit()
            #             else:
            #                 Customer.query.filter(
            #                     Customer._id == customer._id).update({"useBiometric": False})
            #                 db.session.commit()
            #                 ERROR_MESSAGE = "Akun Anda Ditangguhkan, Silahkan menggunakan fitur Lupa PIN "
            #                 HTTP_CODE = 422
            #         else:
            #             ERROR_MESSAGE = "Nasabah tidak terdaftar"
            #             HTTP_CODE = 404
            #     else:
            #         ERROR_MESSAGE = "Unknown Client"
            #         HTTP_CODE = 401
            # else:
            #     ERROR_MESSAGE = "Tidak ada Key Otorisasi"
            #     HTTP_CODE = 403
        # except Exception as err:
        #     db.rollback()
        #     ERROR_MESSAGE = str(err)
        #     HTTP_CODE = 500
        # finally:
        #     db.close()
        # return response()
