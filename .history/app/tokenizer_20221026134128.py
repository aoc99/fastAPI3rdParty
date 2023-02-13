import base64
import datetime
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask import current_app as app
from flask_jwt_extended import create_access_token, get_jwt_identity
# from api.customer.models import Customer, CustomerMail


class Tokenizer:
    def __init__(self):
        self.client_id = app.config["CLIENT_ID"].encode("utf8")
        self.key = app.config["SECRET_KEY"].encode("utf8")
        self.iv = b"5w57Ey2WVcSPDGvp"

    def checkClientId(key_args):
        print('s')
        client = json.loads(Tokenizer.decrypt(key_args))
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

    def createCustomerObject(self, customerId):
        customer = Customer.query.filter(
            Customer._id == customerId).first().serialize()
        if customer["profilePicture"]:
            customer["profilePicture"] = self.encrypt(
                customer["profilePicture"])
        email = CustomerMail.query.filter(
            CustomerMail.customerId == customerId).first()
        if email:
            email = email.serialize()
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
        return create_access_token(identity=self.encrypt(customer["_id"]), fresh=True)

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