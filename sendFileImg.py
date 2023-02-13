import mimetypes
from codecs import encode
import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import requests
import json
import bcrypt
import hashlib
import datetime
from fastapi.responses import JSONResponse

headers = {
                'Accept': 'application/json',
                'Content-Type': 'multipart/form-data',
                'Content-Type': "application/x-www-form-urlencoded",
                'apikey': 'xxk4H7L5pomqPOLLIuZDujr41K9bC15z'
            }
# print(headers)
# payload = payload.dict()
# print(payload)
# photoKtp.file.seek(0)
# photoSelfie.file.seek(0)
# print([('ktp_photo', (photoKtp.filename, open('storage/image/ktp/' + photoKtp.filename, 'rb'), photoKtp.content_type)),
#       ('selfie_photo', (photoSelfie.filename, open('storage/image/selfie/' + photoSelfie.filename, 'rb'), photoSelfie.content_type))])
# print(open(photoKtp.file,'rb'))
# if photoKtp:
#     file_location = f"storage/image/ktp/{photoKtp.filename}"
#     with open(file_location, "wb+") as file_object:
#         shutil.copyfileobj(photoKtp.file, file_object)

# if photoSelfie:
#     file_location = f"storage/image/selfie/{photoSelfie.filename}"
#     with open(file_location, "wb+") as file_object:
#         shutil.copyfileobj(photoSelfie.file, file_object)



req = requests.post('https://apix.sandbox-111094.com/v2/register', headers=headers,
                    data={'email': 'ggjimail@gmail.com', 'name': 'Gaga', 'gender': '1', 'dob': '1989-09-07', 'pob': 'Tasik', 'nik': '32040709890004', 'mobile': '085603179405', 'province': '32', 'district': '9', 'sub_district': '4',
                          'address': 'kopo', 'zip_code': '40225', 'ktp_photo': ('7F648EDD-E966-47C6-8B1E-FBB011CA6564.jpeg', open('storage/image/ktp/7F648EDD-E966-47C6-8B1E-FBB011CA6564.jpeg', 'rb'), 'image/jpeg'), 'selfie_photo': ('Screen Shot 2022-12-17 at 11.34.01.png', open('storage/image/selfie/Screen Shot 2022-12-17 at 11.34.01.png', 'rb'), 'image/png')})
                    # files=[('ktp_photo', ('7F648EDD-E966-47C6-8B1E-FBB011CA6564.jpeg', open('storage/image/ktp/7F648EDD-E966-47C6-8B1E-FBB011CA6564.jpeg','rb'), 'image/jpeg')), ('selfie_photo', ('Screen Shot 2022-12-17 at 11.34.01.png', open('storage/image/selfie/Screen Shot 2022-12-17 at 11.34.01.png','rb'), 'image/png'))])
print(req.status_code)
# if req.status_code == 200:
#     if photoKtp:
#         os.remove("storage/image/ktp/"+photoKtp.filename)
#     if photoSelfie:
#         os.remove("storage/image/selfie/"+photoSelfie.filename)
print(json.loads(req.text))