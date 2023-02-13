import base64
import datetime
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.config import Config
from api.customer.models import Customer
from api.customer.models import CustomerMail
from fastapi.encoders import jsonable_encoder
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


class Tokenizer:

    def __init__(self):
        self.client_id = Config.CLIENT_ID.encode("utf8")
        self.key = Config.SECRET_KEY.encode("utf8")
        self.iv = b"5w57Ey2WVcSPDGvp"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.ALGORITHM = "HS256"

    def checkClientId(self,key_args):
        client = json.loads(self.decrypt(key_args))
        # date_time_issued = client["issuedAt"].split(" ")
        # time_issued = date_time_issued[1].split(":")
        # if time_issued[0] == "24":
        #     time_issued[0] = "00"
        # date_time_issued[1] = ":".join(time_issued)
        # date_time_issued = " ".join(date_time_issued)
        # issued_at = datetime.datetime.utcnow() - datetime.datetime.strptime(client["issuedAt"], "%Y-%m-%d %H:%M:%S")
        # minutes = divmod(issued_at.total_seconds(), 60)
        # print(datetime.datetime.strftime(datetime.datetime.utcnow(), "%Y-%m-%d %H:%M:%S"))
        # print(client["issuedAt"])
        # print(minutes[0])
        # return minutes[0] <= 5 and client["clientId"].encode("utf8") == self.client_id
        return client["clientId"].encode("utf8") == self.client_id

    def createCustomerObject(self, db, customerId):
        customer = jsonable_encoder(db.query(Customer).filter(
            Customer._id == customerId).first())
        if customer["profilePicture"]:
            customer["profilePicture"] = self.encrypt(
                customer["profilePicture"])
        email = jsonable_encoder(db.query(CustomerMail).filter(
            CustomerMail.customerId == customerId).first())
        if email:
            email = email
            customerObject = {
                **customer, **{"email": email["email"], "emailStatus": email["status"]}}
        else:
            customerObject = {**customer, **
                              {"email": None, "emailStatus": None}}
        return customerObject

    def checkAuthorizedCustomer(self, customerId):
        if customerId:
            return self.decrypt(get_jwt_identity()) == customerId
        return False

    def createToken(self, customer):
        # access_token = AuthJWT.create_access_token(
        #     subject=self.encrypt(customer["_id"]), fresh=True)
        return AuthJWT.create_access_token(self.encrypt(customer["_id"]), fresh=True)

    # def createToken(self, customer):
    #     to_encode = {
    #         "id": customer["_id"],
    #         "expired": 5}
    #     expires_delta = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
    #     if expires_delta:
    #         expire = datetime.utcnow() + expires_delta
    #     else:
    #         expire = datetime.utcnow() + timedelta(minutes=15)
    #     to_encode.update({"exp": expire})
    #     encoded_jwt = jwt.encode(to_encode, self.key, algorithm=self.ALGORITHM)
    #     return encoded_jwt
        # return create_access_token(identity=self.encrypt(customer["_id"]), fresh=True)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        if type(data) is dict:
            bytes_string = json.dumps(data).encode("utf8").strip()
        elif type(data) is str:
            bytes_string = data.encode("utf8").strip()
        else:
            bytes_string = data
        padded_string = pad(bytes_string, cipher.block_size)
        cipher_text = cipher.encrypt(padded_string)
        return base64.urlsafe_b64encode(cipher_text).decode("utf8")

    def decrypt(self,data):
        b64decode_string = base64.urlsafe_b64decode(data)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        decode_string = cipher.decrypt(b64decode_string)
        unpadded_string = unpad(
            decode_string, cipher.block_size).decode("utf8").strip()
        if type(unpadded_string) is dict:
            return json.loads(unpadded_string)
        return unpadded_string
