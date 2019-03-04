#解码链接：http://www.vgot.net/test/image2base64.php?

import requests
import getpass
import pprint

url = "http://spoc.ccnu.edu.cn/userLoginController/getVerifCode"
session = requests.session()
json = session.get(url).json()

print(json['data'])
loginName = input('LoginName:')
password = getpass.getpass()
verifyCode = input('verifyCode:')

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

