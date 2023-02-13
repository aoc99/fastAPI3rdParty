import datetime
from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
from fastapi import Request, Depends
from sql_app.database_session import get_db
import json
import base64
import bcrypt
import hashlib
import datetime
import os
import shutil
import aiofiles
from requests.structures import CaseInsensitiveDict
from app.tokenizer import Tokenizer 
# from api.digitalsignature.registration.models import Customer
from app.responses import HTTPResponse 
from fastapi.responses import JSONResponse
from app.config import Config
from pathlib import Path
from app.utils import Multipartify
from requests_toolbelt.multipart.encoder import MultipartEncoder


class ServiceRegDsn:

    def __init__(self):
        self.response = HTTPResponse()
        self.token = Tokenizer()
        self.apikey = Config.APIKEY
        
    async def registration(self, request, photoKtp, photoSelfie, payload, db: Session = Depends(get_db)):
        try:
            
            
            files = MultipartEncoder(fields={
                'email': payload.email,
                'name': payload.name,
                'gender': payload.gender,
                'dob': payload.dob,
                'pob': payload.pob,
                'nik': payload.nik,
                'mobile': payload.mobile,
                'province': payload.province,
                'district': payload.district,
                'sub_district': payload.sub_district,
                'address': payload.address,
                'zip_code': payload.zip_code,
                'ktp_photo':  (photoKtp.filename , await photoKtp.read(), photoKtp.content_type),
                'selfie_photo':  (photoSelfie.filename, await photoSelfie.read(), photoSelfie.content_type)})
            headers = {
                'content-type': 'application/json',
                
            }
            payload = payload.dict()
            photoKtp.file.seek(0)
            photoSelfie.file.seek(0)
            bytesPhotoKtp = await photoKtp.read()
            b64PhotoKtp = base64.b64encode(bytesPhotoKtp)
            bytesPhotoSelfie = await photoSelfie.read()
            b64PhotoSelfie = base64.b64encode(bytesPhotoSelfie)
            image = {'ktp_photo':  b64PhotoKtp.decode('utf-8'),
                     'selfie_photo': b64PhotoSelfie.decode('utf-8')}
            payload.update((image))

            # if photoKtp:
            #     file_location = f"storage/image/ktp/{photoKtp.filename}"
            #     with open(file_location, "wb+") as file_object:
            #         shutil.copyfileobj(photoKtp.file, file_object)

            # if photoSelfie:
            #     file_location = f"storage/image/selfie/{photoSelfie.filename}"
            #     with open(file_location, "wb+") as file_object:
            #         shutil.copyfileobj(photoSelfie.file, file_object)
            
            # print(json.dumps(payload))
            req = requests.post(
                'http://10.6.226.246:25117/api/v1/dsn/registration/register', data=json.dumps(payload))
            # print(req.status_code)
            # if req.status_code == 200:
            #     if photoKtp:
            #         os.remove("storage/image/ktp/"+photoKtp.filename)
            #     if photoSelfie:
            #         os.remove("storage/image/selfie/"+photoSelfie.filename)
            resp = json.loads(req.text)
            return resp
        except Exception as err:
            return self.response.server_error(str(err))
        # finally:
        #     self.req.connection.close()

    async def registerLink(self,payload, db: Session = Depends(get_db)):
        # try:
            headers = {
                'apikey': self.apikey,
                'Content-Type': "multipart/form-data",
                'Content-Type': "application/x-www-form-urlencoded",
                'accept': 'application/json'

            }
            # print(dict(payload))
            req = requests.post('https://apix.sandbox-111094.com/v2/register-consumer-link',
                                headers=headers, data=dict(payload))
            return json.loads(req.text)
    
    async def registerCheck(self,payload, db: Session = Depends(get_db)):
        # try:
            headers = {
                'Content-Type': "multipart/form-data",
                'accept': 'application/json'

            }
            print(json.dumps(payload.dict()))
            req = requests.post('http://10.6.226.246:25117/api/v1/dsn/registration/register-check',
                                data=json.dumps(payload.dict()))
            return json.loads(req.text)

            # print(selfie_photo)
        #     key_args = request.query_params
        #     if key_args:
        #         if self.token.checkClientId(key_args['key']):
        #             data = json.loads(self.token.decrypt(payload.dict()['data']))
        #             passcode = data["passcode"]
        #             phoneNumber = data["phoneNumber"]
        #             customer = db.query(Customer).filter(
        #                 Customer.phoneNumber == phoneNumber, Customer.isDeleted == False).first()
        #             if customer:
        #                 if customer.failedPasscode < 3:
        #                     isMatched = bcrypt.checkpw(
        #                         str(passcode).encode("utf8"), customer.passcode.encode("utf8"))
        #                     if isMatched:
        #                         db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
        #                             {"failedPasscode": 0})
        #                         customer = self.token.createCustomerObject(db,
        #                             customerId=customer._id)
        #                         DATA = {
        #                             "access_token": self.token.createToken(Authorize,customer),
        #                             "token_type": "bearer",
        #                             "data": self.token.encrypt(customer)
        #                         }
        #                         db.commit()
        #                         return JSONResponse(DATA)
        #                     else:
        #                         db.query(Customer).filter(Customer.phoneNumber == phoneNumber).update(
        #                             {"failedPasscode": customer.failedPasscode + 1})
        #                         DATA = {"access_token": None,
        #                                      "token_type": None, "data": {}}
        #                         db.commit()
        #                         return self.response.not_acceptable()
        #                 else:
        #                     db.query(Customer).filter(
        #                         Customer._id == customer._id).update({"useBiometric": False})
        #                     db.commit()
        #                     return self.response.validation_error(
        #                         "Akun Anda Ditangguhkan, Silahkan menggunakan fitur Lupa PIN")
        #             else:
        #                 return self.response.not_found("Nasabah tidak terdaftar")
        #         else:
        #             return self.response.unauthorized("Unknown Client")
        #     else:
        #         return self.response.forbidden("Tidak ada Key Otorisasi")
        # except Exception as err:
        #     db.rollback()
        #     return self.response.server_error(str(err))
        # finally:
        #     db.close()
