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
data = "erg5gpx-Ml3xHC3THg5-qzLZZcv3xXoyFF7SjRwlq5A3cD_r8094CfWeajfNq-GTAupVfTZtZaLL_PLbwKDkkxNY8hAqTR_Z0bQOcZeLRfIo-fh8BpYl_H0MwAs2FhZRKvfBc72M1PdTYUgpr9DixnHWKze3ey2UpH4HsK8Shl1PfbxmQaIJx6G8rc2UQfjnpdHUvqquiyKAYO1V6AR8i-KSwr3Q_OXLIWy6E_w8NTJq-q23QZiEAWx8tFLnLKOyqWMm-wLVKAD37CyfcRKEuDvrOi0iHgmxdJZ_6Rrzr7o63gHPSJYZWr9KuAeUIS-UF420c25rC0ty-ElWGUN1d8ffZQDeRaAybgP5OTznTHTEwjJ0jJmGVxo3P5JeSySoZTVojGlQwFbWIqfnhd4A6RCiXIzB2m4m68j6TaME32VPRhW5wGx7sFDIs4dxW79ZbwapNE6Ov6dBfiQjt1S4oLN1HWNeyrTPgcW4KUiD2pITbpKjJl-3VSARhekNG6w0Udd4pXR3Ds2lwu67H1YFzVd4_u-75B9CFjfSgkNn4XYWHtTCyU3TiTCh-j5LZvulq2kxSGllQs_cE5rijiyK0_6ADARrJM2O_TWstVC5CpTJZPqL4hytHgMfccoMDlBiP8bx92a_ZybFF2xxrJ3WHPiABV4N8HYR1fc902Zlh5cWHCky_GsOkyuuYnZPQU0oWjE1V77rLap2WZKtD2P6JvI_8WZoIlzS1LY6EWvLodeop3IEbCle3K_Um4yuDfUq0djVuiXrQSrYV-6JjJN3TP_YURZNtVRYbHn54xsHKEsMQMTfcPyDmjTC6P3zPdnDAUy51N9VSQNDr_9uzoNbGP1_4-W1gNSpYrYnmT73EPk5cfWnrDCQlWSpyht4_eOWyfg06uPRM-z16pDPhOtiL1bxfme0hRsNn-KmauTy36lmDoVpti-uQcDf2fHf8w_5SOiN98INd2JKxarRzJmQ0jruoGNoyV1I2iXZxwTcrtvbFENvLiCS_YJ8chmk9yHDP6I1iSq17K7o41TjdrPF1u4aiFIxgowgwzKW7x4btAD4RGDJkVwAVrHqvdm9x5Ae134ycFQC--kTqofjmggE3ftg79_hInznQLLpHUo5QglrBibWnw_eC9-VMhjKMx1L7r35H1R3oRTbmFT11jUQOHeDUI-Am_DC2MJyqOmAsUf89xLyxqr91xyxUOWsvoyzUKWMDxB2r7eDdsk-i91x19XXmJN0ZT3j8H5EAZxMvos9FE_1aHm8yXK11mOtGxhjUncye0VguJc_Z_JiOKmtu0bNOLzIkkfRagrII9R7xKMksMZUgs2BgHJVabdRcz_52hybPzAmZoEVRxD0NXHxOiYD3-rnXsVo9YMUX0Y7Pg3ifvp3QKZLISeEfEZJiTuYI8ocZAqkvxhhk1V9pbONkrUWGgmHG1zlaV5X-8SLj3AZx6K8F8pW--QkbDBN4X4Qk5rDIMzMqCMX--65EEFDnAIzGQ_kUIvLTW8dj6HWRUiCLZZqVOdGa4YYbscLP8TXEBKl6vijbu1lYfPHm78JeKOOB7sbOZ2uq3ZYemMbeoxhpw48YXCl-2BCnR1y_wrJrcMsTUmzbuapWJEPpPslNwi8SNVSmlltfcad3sQ94JLb9NLsbpFrLytszetSp-VRKOBjOmnmZ6LQeINZAT_M64ZnVzxdJf7HRd1X_36QZwYFv1OvKykhO3sEfdDhb_fc3_d4CDpWXkpP8X2cQ9clPFcyz6vMFHXoygJ111276ntfGRak_qLlgzHoLJwQRsi5Ooy_dL0eZj2vR2hIk0qxr2DVdTCBouVW4vrE6uTX-G_gqFK3FXpjSuZe4E2e129vUujEVBQSsX2WSeI_gaa55HzdO9lIBp1xJPaDnXNIFo1nb0kQ4unA14tHC10IGPwhWtdMTLekUxdL70lN1domJfbS7D2ck1J2Vcnm7rhKouao12UL_kPtX6-2gqVYc6M-2ORaI2CJYxCPxSEFAFZ5XT60yAyf6RdfIeXFsdMWOZIgJrwhV1S3Rmn687IQ98scSzmOAjsSeXdX5IieBT5KtDuli_CND_hWtWE6OxCaq3_bHQcJti2r8g97R4Qev8axg4oYQ021GPUdY5UtxHyGYZmuzKQbEwd8bSU-UCT2qa40AlDYmrBN3UWBanbeEBsvizd3SOWj5VhuiCdoQ6I-9bLZDHzyqZ6TWriEEYlZNnnMtPFX0OtpP_ocWnxIcnLEC5L1HaHhUk1jNCqsdcI2uw_pIGpKcyeVmv-VVQunnKhvHFEPJhtHa5gOP45cYZRwsDAvo2G6RFPixCQVzknv7rzdcKq2uhTujL0575bG5z-TAPaVOU0OMsIe5wArxFHf8YN5dVmpxRae9P-8fd4nzXcHUro5fVtcZPW5_5eO2AfN8TcE-iEq4vDHZKrP5Hah4xy_Ujd6WNlyZfDsPGCdg0nQxwvESTn350_4ZD0EgbWXBkBYujigAI7z-ZHEUKAqNzzEc5nM00GFXzQCeJH-ZLfcZl4TqYp6pTPllBOgziYrxUYBjmT70yXQiddS5KxKY7qLO_S2MAkPiR1ljYxaX9jPnPTKw254_DHC2fQPZmAgqZQUbUAK19Wx_katqoDShTN8BPrzxADhVC9ymaJ7AIbo186_Ra80eUcH8rMQWsjaoq2It_UNEJRffhT70FpbpZLbmHpVlMD4IsHENv2t8BiW8aM-7FdHYtyovCg345PEkzMgeI9T7mlHhTpK2SCwz63t2JG1HYOURYdZT29kegzjmvuxlLeT2lqarAuWB5MX6S7TZ8kBy_XzD8UA9olT5TeFJf2pUfD0-xQGvuy1xIPs7-btav5EE7XFEGwPHQgC3mEcbogNfo77UQW-YouqcHVPhx4WHz0YlXoKCUFOnrx31CJtV2ieZCkOnBL5U1-lyX2av2VR9hEa-kcXnCbysnhZuCU456uyTAXq_qPlj_AhNpbVFiyNondkwbgWvaVh5q7RS8K4uMwBkWAmPNMECH5gVPU3wjniEWyqFk4qCc8YQvRSLsr216BhruaQGgQz92UVF4mqHB6bLHA4N3Vua4y1TBxh0u_T-FVywcA3j2UkeEH66o-b91EAPpfsLBobMHqt77Qrg5chJSPs2j63KJuxviDCPlqT7ldOG_e-o-Y9PejdrFgWKHXCGXzW5B24Ld4jGfOexlpJYxI6YD4CcmkbfMzfCG2lETmTwQTpv26AZIr7BwCtG3T_xMZQeA3GpaiEmOnvC6CRnCAKZXnvvKkfUXO67PYNV2vWzLa-NwpjN6xIT49TqbP6G8SYyeKJQhLWMMFcFPr4DT2zYHr9ohifRAc00zQwzSl-1Lg9yVUeKe79OdE3VIf2z5E_ZaPdgyyK8xL46WjGSDCO4OtQIV3qxdl3XSxjUmuji0jF930Lxx3Pq9lQwNQVJkaYzufX2xA6fK_Sr6VhVu_1nFYGEpRiexSmkaV8ma91n-_fyPh_wL5h0nSkw4FP-9TlkuVC3yz5dtkBurR9b1_nCDcNXK8Dd6Yqve2OQeRv3hF5ao79Rz6w9xxkZU8Xwny23WzAMTzkvgdVmGCdInXMc5SSro9bbu_dGcJA3wARGR-Ou9nx8R0pbIF2mDPAnaxw9cJBrhKZf8poVuwoPlMLUSVgkRzu38zz6LCoywRSzKpp0P0k-bkbCvv30zJOFCNQJR7Ufby-hUnDt1DKmF8z-3nakKB6mUiV73nt2zSBUpTC1lBAiBuCMEIw0KdX68QDH86nGtYdbwtVyAMNjVPKl3bhhT0vgPQwKiYeSDaqL2tYBUCgtCBHxW7XY7u5fEcoMqFl8TDN3CLBHysTZ_BTDDTBiPaaD3RAsYmYUkBZkuEDdbVykw17Virr3FOGRyh6N5rS9xmR_pYJiYYjlT4lFVynClbW7cqLU3sdtfodixtH_tY32GMehTTxKqKQlX--qahzmXMbHeDovvN6FPcfYdQOb6E2ybeb8bQoNbTIGgTqnuD1TvMGFDG95EbOY6Xi4D97VZmO30uZrade5WGxWuZDp_QBRzZNC2VRp4NlmTnH8xpieINEjZAibd4b4kqc1H-IxpFEl1CB6ER5XNArOofeZuDGgeJgketEEWj_jA87qnaNh-7BX000MHP2y4UuI_7vqtZThbFtxzUJdeXdTEVqvFrq0wuPGFGisqLU3WjyM96Gdpwiw08rCGaKxfmYKPg1vFY0YTiBshEYQfi5Fuj8Qu3OO8pY0zi1s9E8trQG0DPLLM2AUKUP7_Z-321Srph-zNWfGblzA2e3KVMZT_2ZDlOKvcy2mxCYE8OsB-FzFAbVgXyBABcNbeQm3K7WLA3UBPWyQsc8LaCfLTC3rlRkqbLh63UtOGU8nFpnyeteOmm0RTp-B-LG3vsBgY3WltVSnV922kzCFSlt_3WTYq5I0U4G52FNWPr97kD8TsprcmEAqD4hz7J6dsSbw9NMjLxpPKHwMVCh-sq0mcghdWgcqgh5lIf1kSkR9-QrkhLE_EjZ0kYC-DibEEjMYw0vh7j_6GbCK8bNtXPaFWJz7zUi08Vo9flrPGZdIoX0VFMgxlEiv16C4pTabgZuDhR7naxDUj376O1RmjigfHWHggydiXitq9Bd_yJHTLkebK3uubJ0SfcC-J1SrN689htRRDgJMarVrPN4T56bP3-m1DeSkuVb3QCiLc_gmkhomulWH2NPr_cy2P2265u3nmKiwztEZTIUefWcj0R6Mfl3RHpMEPHX_QPRNTYSNN-PkWuF0c08eu_tpHHNpGNZ125IYYhf4gx1xonBU3XU22na52nrXtksQiWT-5TLSXXPrvyJ21XABWnXUw8nBASEPfVggXFbjP_6C1T4aYcuqbWdcT_fC8cwiPGkylEE2JGiDmlWA3W6W91G50DGOhk1B5C7tAfyNiKzlloJowuJPGEqIQsVK0JV129_GB-XKxvjoerThDpKBKt3KL8n5WQmcvK8W5CwraWM_htWUWwgGZTqDIziwaLnEaAOIqMHG744JsaRMnzt4x7oQhhpTscdXdo_Iy1D35sWc-pzVF6TdE1bgkmm6GGbCerw639-FHb0h-aByg=="
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
createTok = json.dumps({"customerId": "46e23467-6f1f-4c4d-b472-02d5bbafbfd8"})
accountNumber = json.dumps(
    {"accountNumber": "0057344830100"})
pas = json.dumps({"passcode": "222221", "phoneNumber": "082222222222"})
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