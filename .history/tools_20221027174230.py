# from app.utils.tokenizer import Tokenizer
import json, datetime
import base64, datetime, json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from requests import get
# from flask import current_app as app
# class Tokenizer:

#     def __init__(self):
#         self.client_id = "m3db2kfGW7Cn0kolJO9WCDV3hls7wc8h"
#         self.key = "12W1m925BSKlGd1TB3eqynDCv2GCy9lp"
#         self.iv = b"5w57Ey2WVcSPDGvp"

#     def encrypt(self, data):
#         cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
#         print(cipher)
#         # if type(data) is dict:
#         #     bytes_string = json.dumps(data).encode("utf8").strip()
#         # elif type(data) is str:
#         #     print(data)
#         #     bytes_string = data.encode("utf8").strip()
#         # else:
#         #     bytes_string = data
#         # padded_string = pad('{"clientId": "m3db2kfGW7Cn0kolJO9WCDV3hls7wc8h", "issuedAt": "2022-01-18 17:46:59"}'.encode("utf8").strip(), cipher.block_size)
#         # cipher_text = cipher.encrypt(padded_string)
#         # return base64.urlsafe_b64encode(cipher_text).decode("utf8")

#     def decrypt(self, data):
data = "UGhJSkEd-esSFS-Clg2ALcUrtg3if8Chh4hS168fo833-Y0R800FUH1-CVyywJpDB7uL6yzO7HduYn7kg4Z7OGzUlPd_EkXSP9dubDDvbTSwAgk4yXjmwUrlPKMAvMNh"
b64decode_string = base64.urlsafe_b64decode(data)
cipher = AES.new(b"12W1m925BSKlGd1TB3eqynDCv2GCy9lp", AES.MODE_CBC, iv=b"5w57Ey2WVcSPDGvp")
decode_string = cipher.decrypt(b64decode_string)
unpadded_string = unpad(decode_string,
                        cipher.block_size).decode("utf8").strip()
if type(unpadded_string) is dict:
    print(json.loads(unpadded_string))
print(unpadded_string)

# token = Tokenizer()
obj = json.dumps({
    "clientId":
    "m3db2kfGW7Cn0kolJO9WCDV3hls7wc8h",
    "issuedAt":
    datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    # "customerId": "57e73c76-c1fb-49b1-adf8-3e24fc116dff"
})

getotp = '085603179405'
refreshTok = json.dumps({"customerId": "fa24e3cd-7c17-4622-8f0c-f4f8935c567d"})
accountNumber = json.dumps(
    {"accountNumber": "0057344830100"})
pas = json.dumps({"passcode": "111111", "phoneNumber": "082115231708"})
cus = json.dumps({"name": "pidi jahad", "email": "ehermanto@gmail.com", "dob": None, "phoneNumber": "085624203225"})
valdatOTP = json.dumps({"phoneNumber": "081214878997",
                       "otpCode": "090121", "keyCode": "aec35005-3150-4f5d-bfbc-6340ec7e1dc5"})
reg = json.dumps({"phoneNumber": "089655295828", "passcode": "111111", "deviceId": "51d6b1b74407ae58", "os": "AND", "deviceProperties": {"version.securityPatch": "2021-08-05", "version.sdkInt": 29, "version.release": "10", "version.previewSdkInt": 0, "version.incremental": "17.0240.2108.103-0", "version.codename": "REL", "version.baseOS": "", "board": "msmnile", "bootloader": "unknown", "brand": "asus", "device": "ASUS_I001_1", "display": "QKQ1.190825.002.WW_Phone-17.0240.2108.103-0", "fingerprint": "asus/WW_I001D/ASUS_I001_1:10/QKQ1.190825.002/17.0240.2108.103-0:user/release-keys", "hardware": "qcom", "host": "mcrd1-13", "id": "QKQ1.190825.002", "manufacturer": "asus", "model": "ASUS_I001DE", "product": "WW_I001D", "supported32BitAbis": ["armeabi-v7a", "armeabi"], "supported64BitAbis": ["arm64-v8a"], "supportedAbis": ["arm64-v8a", "armeabi-v7a", "armeabi"], "tags": "release-keys", "type": "user", "isPhysicalDevice": True, "androidId": "51d6b1b74407ae58", "systemFeatures": ["android.hardware.sensor.proximity", "asus.software.project.ZS660KL", "asus.hardware.touchgesture.swipe_up", "asus.hardware.touchgesture.double_tap", "android.hardware.sensor.accelerometer", "asus.software.soundrecorder.v21", "asus.software.lockscreen.cmweather", "android.hardware.faketouch", "android.hardware.usb.accessory", "android.hardware.telephony.cdma", "android.software.backup", "android.hardware.touchscreen", "android.hardware.touchscreen.multitouch", "asus.software.theme.animated_theme", "asus.hardware.touchsense", "android.software.print", "asus.software.sku.WW", "android.software.activities_on_secondary_displays", "android.hardware.wifi.rtt", "android.software.voice_recognizers", "android.software.picture_in_picture", "android.hardware.fingerprint", "android.hardware.sensor.gyroscope", "android.hardware.audio.low_latency", "asus.software.themes_store", "android.software.cant_save_state", "asus.software.rog.connect", "asus.software.globalaction", "android.hardware.opengles.aep", "android.hardware.bluetooth", "android.hardware.camera.autofocus", "asus.software.zenui.rog", "asus.software.zenui.six", "asus.software.dual_wifi", "android.hardware.telephony.gsm", "android.hardware.telephony.ims", "android.software.sip.voip", "asus.software.preload", "android.hardware.usb.host", "asus.software.twinapps", "android.hardware.audio.output", "android.software.verified_boot", "android.hardware.camera.flash", "android.hardware.camera.front", "asus.software.theme.wallpaper_channel", "android.hardware.screen.portrait", "android.hardware.nfc",
                 "com.google.android.feature.TURBO_PRELOAD", "com.nxp.mifare", "android.hardware.sensor.stepdetector", "android.software.home_screen", "asus.software.sensor_service", "android.hardware.microphone", "asus.software.station.colortemp", "asus.hardware.fingerprint_on_display", "android.software.autofill", "asus.software.inadvertentTouch", "asus.software.smart.reading", "android.software.securely_removes_users", "android.hardware.bluetooth_le", "android.hardware.sensor.compass", "android.hardware.touchscreen.multitouch.jazzhand", "android.software.app_widgets", "android.software.input_methods", "android.hardware.sensor.light", "android.hardware.vulkan.version", "android.software.companion_device_setup", "asus.hardware.display.splendid", "android.software.device_admin", "com.google.android.feature.WELLBEING", "android.hardware.wifi.passpoint", "android.hardware.camera", "asus.software.whole_system_onehand", "android.hardware.screen.landscape", "android.software.device_id_attestation", "android.hardware.ram.normal", "android.software.managed_users", "android.software.webview", "android.hardware.sensor.stepcounter", "asus.software.zenui", "android.hardware.camera.capability.manual_post_processing", "asus.software.sensor_service.terminal", "android.hardware.camera.any", "android.hardware.camera.capability.raw", "android.hardware.vulkan.compute", "android.software.connectionservice", "android.hardware.touchscreen.multitouch.distinct", "android.hardware.location.network", "android.software.cts", "android.software.sip", "android.hardware.camera.capability.manual_sensor", "com.google.android.apps.dialer.SUPPORTED", "android.hardware.camera.level.full", "asus.software.sensor_service.eartouch", "asus.software.smartgallery", "asus.software.airtrigger", "asus.hardware.alwayson", "android.hardware.wifi.direct", "android.software.live_wallpaper", "android.software.ipsec_tunnels", "asus.software.theme.living_theme", "asus.software.gamewidget.zenui.rog2", "android.hardware.audio.pro", "android.hardware.nfc.hcef", "android.hardware.location.gps", "asus.software.pagemarker", "android.software.midi", "asus.software.marketapp", "android.hardware.nfc.any", "android.hardware.nfc.hce", "asus.software.combinekey.forcereboot", "android.hardware.wifi", "android.hardware.location", "android.hardware.vulkan.level", "asus.hardware.display.splendid.reading_mode", "android.hardware.wifi.aware", "android.software.secure_lock_screen", "asus.hardware.glove", "android.hardware.telephony", "asus.hardware.touchgesture.launch_app", "android.software.file_based_encryption"]}})
bytes_string = pas.encode("utf8").strip()
# print(bytes_string1)
# print(bytes_string2)
cipher = AES.new(b"12W1m925BSKlGd1TB3eqynDCv2GCy9lp", AES.MODE_CBC, iv=b"5w57Ey2WVcSPDGvp")
# print(cipher)
padded_string = pad(bytes_string, cipher.block_size)
cipher_text = cipher.encrypt(padded_string)
print(base64.urlsafe_b64encode(cipher_text).decode("utf8"))
# print(bytes_string)
# acc = json.dumps({"accountNumber": "1231231231231"})
# x = token.encrypt(obj)
# y = token.encrypt(pas)
# z = token.encrypt(cus)
# a = token.encrypt(acc)
# print(x)
# print(y)
# print(z)
# print(a)
# print(token.encrypt("085624203225"))