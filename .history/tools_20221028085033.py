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
data = "zXKTpEtnF68QcubDGgpvmVnXFQpqOy6fx5b5Wi_XqJD74STFdqrnXKsAkUlhil5Jg1gHj0MkxgRn-yL0bnlcBS_7GrUjW8IVUDdtqdwQHCfyje2CioljvkNw6mwuS55bIaoRB6eRpiz8nOz5jyqpvsxJcsgGUZoOAnK9ai2mLEDd-tbnXhGjjkbhgrVKrn29ZFcju-YtHaUJ_l6P-tYjL9wzfGOklqiMCQ4t0Kie7v5wFJ-CblYPTawLKSO3W4f-_u2DewvjLBuhJFvkPR0zpfpa9DZ58nHGgCUYB07dqA6MQyq__x1dExRqGaHW9hAP2u2W7GNn1eWeTry85Uz119qTQFpNDSF3V1vi5Gj-EmWrcep1jtw12F7at9MgVi27ki5UraLFSf88CfCicDZN-1Tq6hWcc7n7w_VKWbxPZOKSE_R6mTLCO5398RlTl6YbHskRAfxyu34Y0IbM8BiSvAP5Dqk-t-VrdOZ4V34bjgSWJ-8Y6vrowNAheupViFWUn1auT3w-ferEnjXYX2MdUAf03dlHHz6fvuuB2obNN_IQ_jCfYZ-Rw4NdoLFSSGsX368077JS5xqyuEgg6dN7vYh1f6PxvNvxeqOgTLCA6X2eQWI-iS9W-pWkiK86fsiAhcmls-aES_Ng_fYjFg1fyBlaKG1GVyIObb-EQjBTXY7Efok4DeQoLEjVWT0MmJk3XYH5cS4TlD66KJK4Dtxvop_ztnsHhuwwZWsi6f2jsfMlOo6wkvJRtRbdf4FWVxVYEQXMEiFwGiXRgjmjrihDnI5IZJw3YPbcAmm8QwUc4jEsjXKW5ezIw6rnAY7uq-AHdK9zEkf8ewldgRimAMrLLbj77lAvioGQU2hCYGYhrLUv7RmU-fwUGJQsQGqYlp8aQCrG8xhv8mmKGN7XqKFK53KgdLlnrpsmn1HqRDBRZCn4ORi5R2SU5avN4BkMmtOva5BlmA9WPPQvnwiXcxHwRssC6Z2tgrGhiKEnSbHY8bXOMVCGScSACRvdgeU93jLRnGrMrUffazmoHuqfEc8-kjTWArtUFblKScyOs_AVhKZY4_DkXa9cnjiIrHy1hk2oEheyaxqXGdACPrdqH4WuxlXDSzlzFKfa9mUzMmTe03DkJETNFsa4_w7QrMsB5Tgaklir6xymhCUpVTSQZgfza11rbuMKZ7m2XANI7JaOTveQS4oTgORYVXQx9m6VGDribcj9GkIVdEC1Cf0fNed_4U5zujLYFwAKxHRF-x3JepRA1Uw267LohntzNSjuBVnXVv_DDM05F1eLEDOn0SiQMtSQmqc-MVdnUzcEF11Q5zSNEJN5U6x9jj3JPAxucMdW7H-hUy6q3Jj35un6TRNY__3zO0B6D4N79m0qApKKJ4kX1T4B2IykylSoqQs7p9uKa0s7itLRVYC6TT5BJvsQta0gPNqzaAqFPj2G_sPVyMLEoohs2mDJT-sxTCeKmATyi_2mMbW13o5FMXiNaat7d_C-y5rJsGMQLHAeViwINrBNXJ09D_gxNyEjHQywZu_K7zqbNclTq1bQltuTPwLS1-6vPT7NqRXSVzZvVvh5Y59Pj8dalROJFtccxQx9FJcHMlSp97q0hEcwLxbq7Af-ELhBoS7DgIzbezkRhPpSIZBUdFu3K-Re0f9RsVd8gEh-QDYJtB4-WCtVPEYsDNiS2XLnHpAUl9SUL3EmmYWcgW5Oo9lBM2XShhfQd_yp6r8KHFbnQ-BXNcm1x7oxggeQiwZQ5uvCs5sioQAGHe3azXSNhYa2ZY1W1qSNv91W-PzC4CNk5pBirJ181HEfN0FlWfJzeds1kY5yuT5zNsT-SVlNilBn9JrCy8mYhM6iKDrGOsyeA1syAKZsSfMXzbANDuVg5JoRxcvC1OOwHefWPO88wXWLrLadokBbOxoO1Jc7ggY6NOLOUhYg1H0SHjqPxYBKdsb-SlqqTXqcyRB2Mig1Mzt_3RU8gx7I6qfzi8MzRNopc-TLfSn9yOy4C85tZpClK4aC0OF3vjt18D6YTMglF3eseskTLvugeg3cSj1BvqjQcx4ubSc7qpIre4Jpv8mjfgHDN8yX4ry9mnXQOKeVKayc18Pg4YASRCVAB3AJWQMDaDCLpcl4hIM9-nnUksBWyFS1jYk0wze9AJ8BSFKGKztDggDXztHAV2mZmTfmirlWlA_G1O6xaJ2nnHNeYG7ewzDBbyvivLVtNiEmO6XGQRyU7wF3WuWoPMOCoLD1zYuNBzZw9Bg_s_iLM1sTRXcgXyC3HILUpRm2N1-0yHXEUssWP912AmxaG0CVLDSYAcrZIeKPcIOMEMpfLVZ8U9MFycBMfFO6u4IWIC52OxjCPDSVlzSOoWjPmaAJ0NjRzORKxafYL9lsb5H81GKS-n7129mZuO_iy2nnFJ9BKoPTKe6ExndgaGHYEGRyVA96NgXcMnpWf5rkRcn1vUzgXYOxpD00B16vHv21uSlMU-OwYe2xSLOZAkkTpUuFybsqEGCZD95pW3_KO2KeVnZwTQoLtLyktGwuIcW7Fuwk4es_7m8b9qpLNDIqvKJMh7XhXsfrAVcPP2v0B0dG1HVKdeQh1HEXhBmocE-NFh3Byk3Tpe0qeyEXgjB_tlRIHmS88cXpE61k-52qHmNSlrHKzYK1YJ41jWliRGBsJPgBSIB8wFPFhWmGeUuGwCqZCLX_tpaOBuUgwb-9F3caQ4WjAt1FJ6ma3QR3NPF7_Fp-LhJDMs4nBuQprPP3EJMEckOx918sgcXT7b_31zrtY9mbkN130cxhuddNMNIdUx6n4yykJS-mYRfrSyJDmu68nkV_p_z25dkn6B11s73MeCznsyehMajqjC3dKPOX5jf-FaYFsegN1CvIg_4XXIdJNoCEyPLtS4xvHTsvdGA2H7_hiv3njdHcJnwyT6zN04Qwye1eIwcpFDyDZDa-AcCoPUEz1mo_ZnKP4A1NmbFSIVZnjVBhE0Nz2xyuOH8Mmotdq4s5V1M0-cGBOOGH8zQ8yejIm6STwll7JNabWG0DkH9lm9KTfuVnTChcnM4vmrpNJcS3Fc62u7zEjfkgYP7G78SdMZGTK99kmWodOAG-pqn_XoiDfbOD6W842cnsEImTSztylZQ-TTvbEnWjmQUZq-EXdvst_t332zCN6kJB5sloqC3Bll9tmT4FQ7Pk0idl_1Lhvxc3iZSsNLfTESc9ecj6APwlEo1JV_ItFS-p2V0QA9TONWE3zwJ8BvXNgqqir00BDaQKkWYbVGWv_OYnu79otmPk-iIfLZWEZrz0prSiZYi16OQVyV7aZFlR1J930yMWBK7qFORuzeT8jIZLpf3x2OdZbu3n-d9RcgWypUVcUKgWgtNA4GOV8gCw8c07KdOxYQZNaDG6WWWxmMeOXhEKWioKoMRtNKQkbVSye3hYGyG7qKMJHn0iHv7YgZ3CCWEqR2lK8mrStr6acY6SuA3as2l7-lCgwD75TuON4HlsyXk-sv_z9xvYWActNmzzNIO5oxbFRtnszoe5EAF5-FyKNcaStuQTOb1CgZEhMH3tr5ICY0NBA0qEx6foynvL-eSTdcL9VyeX-EXZ0DxkMK-Ze8zLqJUcf1M70e1wkqJxwvVaDWGyy7SdPDiqSfkrKmVS2g3jSvfmlxu7ciz0VMrTTH_Hd8C-ruUABMpF7PQgES5B6fUt7mfP7vuooMLaNTXf3JA5khfHcnFnrOJwSwl3_lwG84a5mhk4VWNW2StKeGL8RRYBd9jPlMFgV3CLs2nafonw8FU1TLEHenV8FMoiyZ-sjtzefIYUBy34WEMJkfcAkhv6Fb6OHvRhR_tF3hJ8K08LaiFXyxkvfwbM9sJFxYvwNDdNlDcjy6jyZ2P0M5B88hdw92eX9fvV8nk-TvUxv2weH8pEGiY3XKegBYM-OBgurAFgrplLBxXhbpZHOrtwBt3Bvd5F_-4KPd857Do0Ej0Lrw_VJPjd8DPIeg3cPlzMq0sd5vswj1hkowaP8cu-qUgP3lKr2aOBnjZ4c2K2KQoicvWBfo7g2TEvA8l3QZ41R3AvnXnD0kDRxsLMVSSbx17Sr7_0xf9-nSb-0EVFzVY0ItIRagjdysHQT2nT4YW1rgelBJbTuQ4YNOkEiSkezaRYtDXQLPi6dP2fiLGEPSCj_Zk7RuFrPcSQT8IxyrMXnvfUcUpjk1cEdTH05t5WtAJM4G7ELSA-cbhrFRiJ_cttWQisemXo2SaS7gmt2C9iKOMIjTicawRgvpu7HrIrKZ3UyXnb8bTaYMMig_olvGngRaWpwEF6RxerUXd0CX9VhsrhVf302JYo7yA_NWIfiUgY2C_unoH64C1x20xna7550ykt2ltzzCqCYuJVfAlXcJ8TMSNARxiAOFLfZp-E6875uXvQ9JdicBEmWP0FPojoaMtQpznIaB2cKgmSSlUurgQhdOTZyi9A-Bgxo7WjVHkDwF7opZOJiDqRBlEvUTmIFEYGlJTIzBq-t_0K6eUlvdgN7ULb-OCmoAtnzvu65L4yIuHFcImOVzVYtWdWL_RJxF7kSmEOo_qAgYgaC-6wh2Dh9CfbARoINKAY13PGu23VkuT4aj3S4bwlt-awR6SuQHQihjVvV1CE2YBT4LBcPaKEW_i--ToBzuFeJNmH6GjOqqYghU9sTHPVxCYrjDGCr1IDUkyZaxUUPeoH7jGMlwElRw3R9Li02DDu9GOVcBSXwbJNYACbnmL9X_T0ISWqDVWk5alrWJG6v1hRKs4HSj8uZ0ynHpU8YkLCKoU-jx_FrA8DX0D8Un7i97GWPHKNW8bpxnMApggJtv1PV9bDNWGA7vGMGi8F3il4KXjC5nhIpw6iEIU6e51PDTBGZWFJv5bW1ImeJgJpR04uxc8wijuSdWBosGJ1N4uZB0fw9noUm4fKM2F_09VAVgl6zyvqqbyUnti8i6_vYaw12KFNabuUNTmLUDlTonf1e8SNKGejDd5fsfpzjGjFKFOXXr5pKGZFs1wmJBoJHSJSSYQhhffQD53G-NeZCpTGLEo74FCjExeNiPkTaA69Y1gp0up2YiFosm4IKDk_UFh51qvMIurMIerxQEHDuGlWqNh3q8G6eRswFUhVup8UPUPMU9Xt8AW1QI2wDcPDmRaPPs1F51Qm900wvujNbkDZ2ZlTyLfYR3_LTQ8HA7Dbi5N79-yvLpma7IGiKBjPAMZEOkZY7xDCx1hgzPxE6_3m2PLbWxR8pkeluQzH51BfcCBa03gzy_KYVRg_iNB9EtVLKx9TA92Z9r1pmViXhgwjgVt1N2IJKA-IJ0JqeLwutfYOJBzYNtwuW_LMBV3itTSz9chELpl9QFHb1lf5bY9PYN49n1Y04v7JerlnVDTCA1hNd2ZsNhoRhayJ5IstUXTKMszOl7-GyTfME-nBwdlDSmKFz2lppCxJwaMBe2pL7hmnrIufiFogJDhPl7O4rLwruI5JboqsC1bWJKB-UnA8_Z_rYKKndXAdmXRiBBVJFXZw5NEvVcxlsie0CrE-eQORfw-QKr3Y3q5MGzF8rtHz7XGuV5bYis3X1Wb0ORZCvmtl9WXA-Ybh-Gks_ZR-b8FDcZ8mCwOM5_8OPg10EIveO3wpJniHSeTwKNW3L1wpoMWZ1qTEb2bx51sfj2MvBYfo3vk0hgNYMlCtD1MQREAKr-prWBIfVZn71XBKGvjZNuCV5wJGaPXqSOLgzIT5pfJZr6wCwNP41TsyH3G4FrhqdGAmU7qHE4RRsYOiVfw6qjdjDYwXpCH1kopmZ1wQogR1DTqkG9zdUbThIo80dLyJXwsibXrsXzp_kVAmh84xvMx9O2RYo6u6Tc4vlelWbS--qh4_uMZi0qAkQwVG1uP3k0S8a7c0Cq2C_PdODz-cO4A="
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
pas = json.dumps({"passcode": "222222", "phoneNumber": "082222222222"})
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