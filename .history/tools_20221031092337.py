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
data = "erg5gpx-Ml3xHC3THg5-qzLZZcv3xXoyFF7SjRwlq5DTT52h8whSeJR2UujTcOrOil9aRETlYZL9PFaJTil7LQI_dNzdyGj_KFj_vvNQ5zjfFFMBSJf-05i90mO8LgwjBpNR-9L2_CFGjfHKAHrP7fxdK_NrP5zSUt7rVk5wiDrFnXaZ0ChrI_mtge9ffQ7M_i0iIBHNGR-avQQdnEznroU5v7ypvGHXTAkqlsL3075xJEM4kXAkYs5O74_cF4vcGADePQAE4HB3PHr9kdpEeHRpn40XBj1FjO6ZcxlmzG_2BxqYlwgzjoCSGehCUlkyDGpr0qWzQSYGmfBW3QqHUj2SFm9vYF3mT6eR3bf2qWeRT0p6PCfemRzFz6x-jw1uv65eI2Zz7mPhPjfb4_ubEsgErInVJtpJd8ndSuqJNGCqpvduHoa7VknOEkbwK5m3px0FExDeKq5VrW4bKJkJs5ZYxixcWaG1xT0V0-DoGjTwsAcBy1I9f54wsLBC224m09vVJPRQoD58OHXYySAMdJN_Wf__tGdF61zNc-24ad6xRZbBHwT3xXsYmrE5pIH5QU_upGIgse9s1DXXS6rkEFbdLcoMu9iKg1old_g1VqfDsa8tOGwihzxS4s-WaqUmiyvHikyBJBx8VwqpCRfOEgLfs7r-v9BEFw_q-rlkgjATydzDfwTc61vfqzLuGoo5XatBt185RzFjRkyxNxZL51mbNyr_r1LZ6748wmR-qk1BWb0-iL643-FqcTd69w519KO6Q8Q7_qy1C5VGA8_MnAyV4b8oBFWHeoAwdyH192UJLXUlkJE3VTP2EMUS5eDy5zoAHVrP_sK3kY_q8YWK7jM1e41tnmTHWaIdWqSOMnoH6uhI4aq_lIuv9D_LQT9anDHxHUxV6uipwudJNVgQiUKZv78pmkkrLH_D-pV5BqTaoDQM3xyTDiV4L3j6I-FBpRh1Wx2rxI8yJYBK2SyCh0TrTfltdUnnHMvQ7430lwhO1Ywg7l-fpPH7YJxXLmWZLI7Ryw0AaGIsBec_iInRI7fwOt1OqtDJ6uBDUXcpKXnV9MjNH0rUMkD-MIfijRElAR43PHcR9Xl0NJ4l2utpeofK-FqbycBLt0T2CCMs6VTX-RSZw2FqKBPIUISPxs-fx_Sw1WN44_TjLYYGzyjveVLZ-o7zVxmnU4GplMQL-az0TFviznfSiF1cCgdBp-C7-LPytQFnVpLiL9Wfrt6Ae6G-nck7UON2Rct5xo-a1lMuuHQIhBZ-MS5TjmSUT7kuliYSezn6_f-oW9N9Ti5hsgXzprwuLw8_LpjQIjt0yXoX_u9ryH8k7oD7FUqftcdVy3Zc9dW30WIArF4WSEJcJfF8eUGdx0onJDCnPe-Cd7eUrTMmhWmkinvgRyJIpBml9wPJeFNVedGdrANfizARJEFIyCLH-aGtoY4AVftdRuEk_Lj_w7Xl0ycp933qiiHuW7gZVY1cwnoFVPO5aLXQgBsawL-ryUokqB_cnvhoMnAJwldp_2Xe2wih-XQYYmC4vps61Z4MSND50kw5m2Q6uGBKvxSDhf7izYzLQwYxDYhHkrGJ36J4q6X9zHfutDKeBjuMttdcU5h1g5tMdXxCni06lx0Xat322nI1nqidUBvEw7bsAH64KZkN4_1fsE6hdpg-09CkZy44sgFzjlErwUkeKijfHAtscyRZH51cJbnlLTVKOGS4a0dqjKmDLx_Jk2uk8FcO_zKu7cUo5GDktakLNzJdhnzG9FdsV2N0m22n4mMF33hI3gYQ8BHbmlspz8JE0isgPPtAgjesnobS6C_dA9gCfbz2dINOwhlP2Am2OCziB4KrQvWJpczJhfj7Q_9wmcVEqJEMfJzXZPj898QLBPbgaZQ6z840bjTH3LScyAHUQW6ssysHBXYPwTAQEi1vW0lm7E3YvEPpmRxhSW2gVr2YIhWOCVddYQbM5RSLebuBbkyaxwFbYKcZc1Dk8xssMv2GnJC-1Qb4N2-d_S460ylp7mdJNAjh3uCfZCDfOjhTM5p-Cs57vsO3H8gDAqhPFDdj7bIFDdDvkTN2UnO4bDwXrs1G8QuqzOz1ciDbH2fvUTJiNI27bv-LadrlrpXVPA-UZYy4uPfxsi9miqHUMdET2dcilaqCGEoX-wc_fPIQ1s2UOAuCFBQlxuWFANr0VVZHVDA4ZE6ZcgUs6CDE2w3YMXbMuzazIO_3CSjZYh2FxkVbkPDtg-w-SHQabb3jqrxDbqoRXQKR5fDroBBaRr5t7llryE4-qTziiQNyUnYIi1nVdm4OpztxVc5ZI-9NhTdVdsj1afnHpXLApcUgY8tLqW6mCxpXqR98q7llsidm0fNbc8T5klkx2qGLNCaSJ1ndbvm2J3hU26NyHJwQL5TWrznyqgIoX7w0B6iERWZB_ZAwGrvxggBsx2L6MskKrJ2r1sqv8sf1I843wW2J0b4b_FozJlflpm7C64jAmJmbywOo6-iReYEXhMsW7m70fmb83iMuPB0Zhb4l0GcijUsEPfhOPvd8WrEXZ2QaUQXkQ_gVVEweSXPEEEBfyVr7IJgYmuGsNX6d2rnL5I_d9ZIjKoQ30r4NQRaAo-qB8SNmQ1DtXKCiT6Air2We9Cnx0KZFWarBs9OTxo2_2e5PLp9pv7-H2scdnTJD3uOLE_-up05kwhzMwXB2cQF1giTMfjN_bIE2W8v_o8Q8xwCYHhHVN2G76B73gP3GYeNgDAnNl3WqFPYz8jjTdZbx9PYkgzz0wbmcZjI6ZrfjuV_H0knPgGBPEPUEvpto-7uIHhws5ifBqMWpAAn196qxUUBaWaMMjpNJctt8aMar_sGWCw1jKf5aZP1htaIgzYNzNXNUZO9jBYtAlH5ns1nLYqSSoS-H8ZUhjfUlTsOAfj2mE_3MW8XeOaS1_9E-DeJ8Q6SreW12MkoWmVRkYcFRCcX2yC2NjnJo-E6xN74vjxGHGipsONGAvTRCzFPcJVkG8Db9f0d-REs8Faa0_DhqP7Lz7-cXTdOiwObSZTG6xa8LuCVaYIS4VQlcSKjLl04dTRtsyQy0PLd6j3Oev-J3Diod5JswvzhnHq07_7FXj11NmzpLFZV-fbNbC7cKWdCcRn_1kBxRR7KWVmnxmCDVWer7d5s0Jmg7AIRH5DR1eeIOb8z15LMzAS9Zr7ODETVVHVn5yt-PxWKWhOpPffMvN9GpkyySQn7FYD8QgvlN5kWBVDzaHqhLaQsZspsWU5wQxWR5MbKu0oYYtitcb-EhRcIPHR5othc9r7hcOCRR14I9H3zX09qJbCHam5S9UezCRu750Rx6H2gflDEo-giDVjmIqqyTOnfL3yVHcm5suLTAEkelFmcivIoVDw3C7fJ9RvxVHnGZNWPFPYOftyFkvIXxAB6j480PNc32RqHkcb8DGfg1iK-BBQJe9G61leOXwy27R3c6OAPvcTjZ3fAGy3xBk7zDE56BCYfoVLQwybW1coe6cKHvU0GBGlvlm9VAgkt7Ykfin-_Ji2KT3am71MPLEXcQV-qRrhwFeAwRmCpz8tHIRMWG_BES6_m4oaluXW9P8p9p8eJTog-doho6HZNUH2gTSjSyXPQIhnZHNRxhwn3MTSfyJoJfVxXo7rexBwEAT0QVbSFTE2ZA2YZWLyh6FX2p6Xz_OSMD65gvZ_3x3a291M-7Iuko3O9-1yLpNnXwTTUDNkgTeSPWEd6hKBkRo1oV-XvM2pI0fFL2j-X9aBBdwwCLbQJV6cDViFx_DRB7o7VWO5studsHjMxdy5ecoeCZHzsk9svox-ZrRxcDLE4VrVjPVRtPJYF2qQ-LZJ6-JZUPIHXbkW479M-F0sCF1FdnPl-2kA12UywA26qxSDmIWdsCRYU0wqNvaZfS64B7XxDr555UZbthE5NRyLxnyY5lfuFke_lPD2F1_OHZqD6teCdrIkNVqBrre7ha_gChN73a_9Hd8yPWJEBKroSzDz2_xCVtHQoGZGzI3dVymryWLQ24O6yKAizetc3Tiw62rRtyvM9XL9nEpmM0wWtq5Liwq0xCBafAGd-ZEzVbQEBrwxjU7p4pIH05O4pDmZdvZRvsDtt_hm09HJsEpOwzvp5MOfIskS1GDTB92_045pGWOtLVQYwHlbk2-EJZ40NikhDXLjLU8mttn9f9WbYOhRv2nxK_s_2rRVOdGphF0XC6yZppE6rC6fto0yDdsWXFRUP8CdOS1u3VjaZ9pDFVhVUEF0VKh718b7swjR8xLneNdaCeF0yhKB6NLosJjc3_Vx46E-C2TYaXXf9APcQesbpm_6dCadIHlnPVS2nHL7q3Qz7P2nstOONtcjlwhr6Aty3rrI6gfZZ1_2KYm4RG7Qn7fMtm7RRrIElVRzsLtpsUgII67TzZAHNDEVBqdjSg0goMEtBKhx_DYrh6wc4VIOwTagYipqsVm1r9SOmADkM-zQEq9iF1EqF39k0jbSMSATggvA8DpoDdxQntqFKFDL4BmSn3xl4xSq99g6CMqXRBFv2Zi899ZdNagj5yhXsbCVjer2Nr7HuVXSVD29xWyoVZoYIsceIqD24dmzT8PHoRuxyAupL2cLTajPU2JQiqOZq-byWwc4Tpq9OMa_wHLvPwx_eVpbQizV_TAf3fU_D6RnnjK2nY7vqLH1l9tbtWCAWTXU_2rQOy-eiJdh7k8T2iO0RN2Glq2kpvbCxN8K68OXbOmPBQ0sqdCGeoiKjU5vwH1j6_Nvza_X-Ujf95wlAtqYJ-3sgnq9BPjJtvAoKhVmknOtrO46xNwr6V82JjS3mqwdC7MENk-5wJwj9a_k8fn7hXRpZuItclPfFoxvrZYVN7X8IiNflXwbq14Q7M5iP7lA3r_6rR8a40zTVikeB-h3v6k4F7OwfUlgHZza_Yp-6DO4uqflMXFUCOtGE3aL48bCV9wKX1QWA5yjsfdVfWHJ4WxOtQmemB0WGWXgXiGjV96uQPmFeS1DCOWpibVGSapvO41NWvU0QxKASa6U1e4KoVxxTkv6z0JwaOMfpDJpCktqv0cZDjgFow51aIjQdsCIev8jo9TY29jjrEsy2XPaLH-vWBTipLAy_PEZMLC4asbqZSEN_0pyqYKV7-faNA4fcc4dZZt4YzaxIx1R7F9c4lZY_KoFlnV-fAodIHAE_laMxJvu27ZiE="
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