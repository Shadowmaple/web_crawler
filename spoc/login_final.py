import requests
import getpass
import pprint

loginName = input('LoginName:')
password = getpass.getpass()
# password = loginName
payload = {
        'loginName':loginName,
        'password':password,
        }
session = requests.session()

url = "http://spoc.ccnu.edu.cn/userLoginController/getUserProfile"
rp = session.post(url, data=payload)
status_code = rp.json().get('code')
if status_code:
#    print(rp.json())
    print('登录失败！账号或密码错误！')
else:
    url = "http://spoc.ccnu.edu.cn/userInfo/getUserInfo"
    rp = session.post(url)
    info = rp.json()
    pprint.pprint(info)

    userId = info['data']['userInfoVO']['id']
    url = 'http://spoc.ccnu.edu.cn/api/friend/getInitList'
    params = {'userId' : userId}
    r = session.post(url, params = params)
    pprint.pprint(r.json())

