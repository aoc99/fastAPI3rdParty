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


class ServiceCustomer:
    def checkpasscode(self, dataReq, request ):
        # try:
        key_args = request.query_params['key']
        print(key_args)
        #     if key_args:
        #         if self.token.checkClientId(key_args):
        #             data = json.loads(self.token.decrypt(data))
        #             passcode = data["passcode"]
        #             phoneNumber = data["phoneNumber"]
        #             customer = Customer.query.filter(
        #                 Customer.phoneNumber == phoneNumber, Customer.isDeleted == False).first()
        #             if customer:
        #                 if customer.failedPasscode < 3:
        #                     isMatched = bcrypt.checkpw(
        #                         str(passcode).encode("utf8"), customer.passcode.encode("utf8"))
        #                     if isMatched:
        #                         Customer.query.filter(Customer.phoneNumber == phoneNumber).update(
        #                             {"failedPasscode": 0})
        #                         customer = self.token.createCustomerObject(
        #                             customerId=customer._id)
        #                         self.DATA = {
        #                             "access_token": self.token.createToken(customer),
        #                             "token_type": "bearer",
        #                             "data": self.token.encrypt(customer)
        #                         }
        #                     else:
        #                         Customer.query.filter(Customer.phoneNumber == phoneNumber).update(
        #                             {"failedPasscode": customer.failedPasscode + 1})
        #                         self.DATA = {"access_token": None,
        #                                      "token_type": None, "data": {}}
        #                         self.HTTP_CODE = 406
        #                     db.session.commit()
        #                 else:
        #                     Customer.query.filter(
        #                         Customer._id == customer._id).update({"useBiometric": False})
        #                     db.session.commit()
        #                     self.ERROR_MESSAGE = "Akun Anda Ditangguhkan, Silahkan menggunakan fitur Lupa PIN "
        #                     self.HTTP_CODE = 422
        #             else:
        #                 self.ERROR_MESSAGE = "Nasabah tidak terdaftar"
        #                 self.HTTP_CODE = 404
        #         else:
        #             self.ERROR_MESSAGE = "Unknown Client"
        #             self.HTTP_CODE = 401
        #     else:
        #         self.ERROR_MESSAGE = "Tidak ada Key Otorisasi"
        #         self.HTTP_CODE = 403
        # except Exception as err:
        #     db.session.rollback()
        #     self.ERROR_MESSAGE = str(err)
        #     self.HTTP_CODE = 500
        # finally:
        #     db.session.close()
        # return self.response()
