import requests, json, httpx
headers = {
                'Accept': 'application/json',
                'apikey': 'xxk4H7L5pomqPOLLIuZDujr41K9bC15z'
            }
payload = {'email': 'ggjimail@gmail.com', 'name': 'test1', 'gender': '1', 'dob': '1988-09-07', 'pob': 'Tasik', 'nik': '3204090709890004', 'mobile': '6285603179405', 'province': '32', 'district': '9', 'sub_district': '4', 'address': 'manchester', 'zip_code': '40225'}



files ={'ktp_photo': open('../../../storage/image/ktp/Screen Shot 2022-12-17 at 11.34.01.png','rb'), 
         'selfie_photo': open('../../../storage/image/selfie/Screen Shot 2022-12-17 at 11.34.01.png','rb')}

req = requests.post('https://apix.sandbox-111094.com/v2/register', headers=headers,
                    data=(payload), files=(files))
print(req.status_code)
print(json.loads(req.text))