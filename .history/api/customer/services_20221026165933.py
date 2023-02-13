from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
import json
import bcrypt
import hashlib, datetime
from requests.structures import CaseInsensitiveDict
from app.tokenizer import Tokenizer as token
from api.customer.models import Customer 


class ServiceCustomer:
    def checkpasscode(db, dataReq, request):
        # try:
            key_args = request.query_params['key']
            if key_args:
                if token.checkClientId(key_args):
                    data = json.loads(token.decrypt(dataReq.dict()['data']))
                    passcode = data["passcode"]
                    phoneNumber = data["phoneNumber"]
                    customer = db.query(Customer).filter(
                        Customer.phoneNumber == phoneNumber, Customer.isDeleted == False).first()
                    if customer:
                        if customer.failedPasscode < 3:
                            isMatched = bcrypt.checkpw(
                                str(passcode).encode("utf8"), customer.passcode.encode("utf8"))
                            if isMatched:
                                Customer.query.filter(Customer.phoneNumber == phoneNumber).update(
                                    {"failedPasscode": 0})
                                customer = token.createCustomerObject(
                                    customerId=customer._id)
                                DATA = {
                                    "access_token": token.createToken(customer),
                                    "token_type": "bearer",
                                    "data": token.encrypt(customer)
                                }
                                print(DATA)
                    #         else:
                    #             Customer.query.filter(Customer.phoneNumber == phoneNumber).update(
                    #                 {"failedPasscode": customer.failedPasscode + 1})
                    #             self.DATA = {"access_token": None,
                    #                          "token_type": None, "data": {}}
                    #             self.HTTP_CODE = 406
                    #         db.session.commit()
                    #     else:
                    #         Customer.query.filter(
                    #             Customer._id == customer._id).update({"useBiometric": False})
                    #         db.session.commit()
                    #         ERROR_MESSAGE = "Akun Anda Ditangguhkan, Silahkan menggunakan fitur Lupa PIN "
                    #         HTTP_CODE = 422
                    # else:
                    #     ERROR_MESSAGE = "Nasabah tidak terdaftar"
                    #     HTTP_CODE = 404
        #         else:
        #             ERROR_MESSAGE = "Unknown Client"
        #             HTTP_CODE = 401
        #     else:
        #         ERROR_MESSAGE = "Tidak ada Key Otorisasi"
        #         HTTP_CODE = 403
        # except Exception as err:
        #     db.rollback()
        #     ERROR_MESSAGE = str(err)
        #     HTTP_CODE = 500
        # finally:
        #     db.close()
        # return response()
