from email import header
from urllib import request
from sqlalchemy import false
from sqlalchemy.orm import Session
from . import models, schemas
from api.auth.models import ParameterUser, ParameterUrl
from api.auth.services import Token as serviceToken
from fastapi.encoders import jsonable_encoder
import requests, json
from requests.structures import CaseInsensitiveDict
from app.utils import validate as Utils

class Peserta:

    def getPeserta(db: Session, peserta: schemas.PesertaBase, skip: int = 0, limit: int = 100):
        if Utils.validateToken(db):
            try:
                getToken = db.query(ParameterUser).first()
                Token = jsonable_encoder(getToken)['token']
                Url = jsonable_encoder(db.query(ParameterUrl).filter(
                    ParameterUrl.module_code == '2221').first())
                header = {'Authorization': 'Bearer ' + Token}
                # header = json.dumps(header)
                body = peserta.dict()
                print(json.dumps(body))
                proxies = {
                    "https": "https://10.12.14.8:3128",
                }
                send = requests.post(Url['url_address'], headers=header, data=json.dumps(body), verify=False)
                print(json.loads(send.text))
                print(send.status_code)
                return send.json()
            except Exception as ex:
                return str(ex)

    def verifikasiPeserta(db: Session, peserta: schemas.VerifikasiBase, skip: int = 0, limit: int = 100):
        try:
            getToken = db.query(ParameterUser).first()
            Token = jsonable_encoder(getToken)['token']
            Url = jsonable_encoder(db.query(ParameterUrl).filter(
                ParameterUrl.module_code == '2222').first())
            header = {'Authorization': 'Bearer ' + Token}
            body = peserta.dict()
            send = requests.post(Url['url_address'], headers=header, data=json.dumps(body), verify=False)
            print(send)
            print(json.loads(send.text))
            print(send.json())
            print(send.status_code)
            if send.status_code == 401:
                serviceToken.GetAuth(db)
                send = requests.post(Url['url_address'], headers=header,
                                    data=json.dumps(body), verify=False)
                return send.json()
            else:
                return send.json()
        except Exception as ex:
            return str(ex)


    def verifikasiFPeserta(db: Session, peserta: schemas.VerifikasiBase, skip: int = 0, limit: int = 100):
        getToken = db.query(ParameterUser).first()
        Token = jsonable_encoder(getToken)['token']
        Url = jsonable_encoder(db.query(ParameterUrl).filter(
            ParameterUrl.module_code == '2222').first())
        header = {'Authorization': 'Bearer ' + Token}
        body = peserta.dict()
        send = requests.post(Url['url_address'], headers=header, data=json.dumps(body), verify=False)
        if send.status_code == 401:
            serviceToken.GetAuth(db)
            send = requests.post(Url['url_address'], headers=header,
                                 data=json.dumps(body), verify=False)
            return send.json()
        else:
            return send.json()
