import datetime
from sqlalchemy.orm import Session
from . import schemas
from fastapi.encoders import jsonable_encoder
import requests
from fastapi import Request, Depends
from sql_app.database_session import get_db
import json, base64
import bcrypt
import hashlib, datetime, shutil
from requests.structures import CaseInsensitiveDict
from app.tokenizer import Tokenizer 
# from api.customer.models import Customer
from app.config import Config
from app.responses import HTTPResponse 
from fastapi.responses import JSONResponse
from PDFNetPython3 import *
from typing import Tuple


class ServiceSign:

    def __init__(self):
        self.response = HTTPResponse()
        self.token = Tokenizer()
        
    async def uploadDok(self, Authorize, payload, db: Session = Depends(get_db)):
        try:
            headers = {
                'Accept': 'application/json',
            }
            payload = payload.dict()
            print(json.loads(payload['signature'])[0]['detail'][0])
            payload['document'].file.seek(0)
            bytesDok = await payload['document'].read()
            pages = tuple('2')
            x_coordinate = 382
            y_coordinate = 553
            signatureID = 'Gaga'
            # output_file = "storage/document/" +payload["document"].filename[:-4] + "_signed.pdf"
            # PDFNet.Initialize('demo:1674530712619:7d5d23250300000000051fa0959ac4a7386db5d419de9bcfcfa1c463d6')
            # doc = PDFDoc("storage/document/"+payload["document"].filename)
            # # Create a signature field
            # sigField = SignatureWidget.Create(doc, Rect(
            #     x_coordinate, y_coordinate, x_coordinate+100, y_coordinate+50), signatureID)
            # # Iterate throughout document pages
            # print(pages)
            # for page in range(1, (doc.GetPageCount() + 1)):
            #     print(page)
            #     # If required for specific pages
            #     if pages:
            #         if str(page) not in pages:
            #             continue
            #     pg = doc.GetPage(page)
            #     print(pg)
            #     # Create a signature text field and push it on the page
            #     pg.AnnotPushBack(sigField)
            # # Signature image
            # sign_filename = "storage/sign/"+signatureID+".png"
            # # Self signed certificate
            # # pk_filename = "storage/sig/+container.pfx"
            # # Retrieve the signature field.
            # approval_field = doc.GetField(signatureID)
            # approval_signature_digsig_field = DigitalSignatureField(approval_field)
            # # Add appearance to the signature field.
            # img = Image.Create(doc.GetSDFDoc(), sign_filename)
            # found_approval_signature_widget = SignatureWidget(
            #     approval_field.GetSDFObj())
            # found_approval_signature_widget.CreateSignatureAppearance(img)
            # # Prepare the signature and signature handler for signing.
            # # approval_signature_digsig_field.SignOnNextSave(pk_filename, '')
            # # The signing will be done during the following incremental save operation.
            # doc.Save(output_file, SDFDoc.e_incremental)
            # b64Dok = base64.b64encode(bytesDok)
            # payload.update({'document': b64Dok.decode('utf-8')})
            # print(json.dumps(payload))
            # file_location = f"storage/document/{document.filename}"
            # with open(file_location, "wb+") as file_object:
            #     shutil.copyfileobj(document.file, file_object)
            # req = requests.post('http://10.6.226.246:25117/api/v1/dsn/sign/upload-dok', headers=headers,
            #                     data=json.dumps(payload))
            # resp = json.loads(req.text)
            # return resp
        except Exception as err:
            return self.response.server_error(str(err))
    
    async def signing(self, Authorize, payload, db: Session = Depends(get_db)):
        try:
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'multipart/form-data',
                'Content-Type': "application/x-www-form-urlencoded",
                'apikey': self.apikey
            }
            payload = payload.dict()

            # file_location = f"storage/document/{document.filename}"
            # with open(file_location, "wb+") as file_object:
            #     shutil.copyfileobj(document.file, file_object)
            req = requests.post('https://apix.sandbox-111094.com/v2/url/sign', headers=headers,
                                data=(payload))

            return json.loads(req.text)
        except Exception as err:
            return self.response.server_error(str(err))
    
    async def signing(self, Authorize, payload, db: Session = Depends(get_db)):
        try:
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'multipart/form-data',
                'Content-Type': "application/x-www-form-urlencoded",
                'apikey': self.apikey
            }
            payload = payload.dict()

            # file_location = f"storage/document/{document.filename}"
            # with open(file_location, "wb+") as file_object:
            #     shutil.copyfileobj(document.file, file_object)
            req = requests.post('https://apix.sandbox-111094.com/v2/sign/bulk', headers=headers,
                                data=(payload))

            return json.loads(req.text)
        except Exception as err:
            return self.response.server_error(str(err))
