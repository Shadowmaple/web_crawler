import requests
import getpass
import pprint
from verifyCode_test import connect as vcCheck

url = "http://spoc.ccnu.edu.cn/userLoginController/getVerifCode"
session = requests.session()
json = session.get(url).json()

loginName = input('LoginName:')
password = getpass.getpass()
verifyCode = vcCheck(json['data'])

payload = {
        'loginName':loginName,
        'password':password,
        'verifyCode':verifyCode
        }
url = [
        "http://spoc.ccnu.edu.cn/userLoginController/checkLogin",
        "http://spoc.ccnu.edu.cn/userLoginController/getUserProfile",
        "http://spoc.ccnu.edu.cn/userInfo/getUserInfo",
        ]
for url in url:
    rp = session.post(url, data=payload)
info = rp.json()
pprint.pprint(info)

