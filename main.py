#importing librarys
from flask import Flask,request
import requests,json

#Creating App
app = Flask(__name__)

@app.route('/',methods=['get'])
def tt_chack():
	email = str('jajaj@yahoo.com')
	email = str(''.join([hex(int(x ^ 5))[2:] for x in email.encode('utf-8')]))
	url = 'https://api22-normal-c-useast1a.tiktokv.com/passport/email/send_code/?residence=IQ&device_id=7092527186544330246&os_version=15.3&iid=7169698265780471557&app_name=musical_ly&locale=en&ac=WIFI&sys_region=US&js_sdk_version=1.77.0.2&version_code=19.3.0&vid=C6A977A1-AC7C-4D0E-9533-1FCD3972CE85&channel=App%20Store&op_region=US&tma_jssdk_version=1.77.0.2&os_api=18&idfa=00000000-0000-0000-0000-000000000000&device_platform=ipad&device_type=iPad8,9&openudid=b15d01695de61d898e7774d0bebb7616eb7c669e&account_region=&tz_name=Asia/Baghdad&tz_offset=10800&app_language=en&current_region=IQ&build_number=193021&aid=1233&mcc_mnc=&screen_width=1668&uoo=1&content_language=&language=en&cdid=1C0B1ED2-B24D-45E6-8FE6-61C3D7E914B2&app_version=19.3.0'
	headers = {'Host': 'api22-normal-c-useast1a.tiktokv.com','Connection': 'keep-alive','Content-Length': '94','x-tt-dm-status': 'login=0;ct=0','sdk-version': '2','passport-sdk-version': '5.12.1','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'TikTok 19.3.0 rv:193021 (iPad; iOS 15.3; en_US) Cronet','X-SS-STUB': 'D7CE342D11D9F8D71317CB6018E0723B','x-tt-store-idc': 'maliva','x-tt-store-region': 'iq','X-SS-DP': '1233','x-tt-trace-id': '00-b3846c2110626db7e5f9c68606b204d1-b3846c2110626db7-01','Cookie': 'install_id=7169698265780471557; ttreq=1$493562f43587bf8f4ab1ad295bb07928d4f38c8c; odin_tt=8d0272d7553283b7921b0db2f20f540ad3ea35c499e7636045cfc42d18c0c2ae09355cdd56e2a74ee2989f0e22f800008bdcf777b7ad717bc5d7bf3225c3018af5615e7272cc92715075685d81ce21b9; passport_csrf_token=4de597e1dae77056b0e7c21f827b7079; passport_csrf_token_default=4de597e1dae77056b0e7c21f827b7079; store-idc=maliva; store-country-code=iq; store-country-code-src=did; tt-target-idc=useast1a; tt-target-idc-sign=dFk5sgqrt9Y3MIS0RLCY0g-2601CkNzWw_Ii1qzJYi9KLO5NpylaJk5DueaHcZpQQX7PT6iVeNSGEEVH-Uy8Yk-NMrOlLjM0t2vx5TuMc_wnjwutSaLVF63WOZ3o3KVg8mBhRcWhEzxFm2aD1NZNXj6WRGalB08OZ9cd8DVSnFkz6e-9GOpQZZsCrOcqG5L4lYO2GI8vSUOBk9EtTEZ3kc6UNxfct2odJsHOqnnVzuASZjBF7yE-10kklJnjLfshyI7prj620zXJxz4CXC-c6uTedC6WPSvYhP1TVl7x-76Gi5r0fVqvO9CAR3ajfXSrSygsDvlGfh-ZlRq5IE8FiWeTkGdRVfbCfQijnCYHrgfbXbzxcdllkM_0tBNII9xpUtpemULpGVipz5DxSg5KMiaNJXalnc1_XcHCOgcv6fzs1_iUD9cqdUFemHLEV697FSnISyeqNtS_MfxdzcTsyFKig6EV1IJ5H2JzbqNJV07Bx3srcSFCLnwtaqmt1go5; msToken=0j-quCfGSneK7O03RCWimE-aNaj5E9rNecnU9G19aryHpKG0cHZZWTg4MEw5ywGfnzJxIZMRTZtRGGhAO6AK00T6','X-Khronos': '1669459110','X-Gorgon': '8402c033c800583cb285dc0fc322fccb7b5b9e64a323de5b8c4e'}
	data = f'account_sdk_source=app&email={email}&mix_mode=1&type=31'
	response = requests.post(url,headers=headers,data=data).text
	return response
