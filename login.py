import requests
import getpass
from bs4 import BeautifulSoup

username = input('Uesrname：')
password = getpass.getpass()

#url = 'https://account.ccnu.edu.cn/cas/login?service=http%3A%2F%2Fone.ccnu.edu.cn%2Fcas%2Flogin_portal'
url = "https://account.ccnu.edu.cn/cas/login"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
cookie = r.cookies['JSESSIONID']
lt = soup.find('input',attrs={'name':'lt'})['value']
execution = soup.find('input',attrs={'name':'execution'})['value']

payload = {
        'username':username,
        'password':password,
        'lt':lt,
        'execution':execution,
        '_eventId':'submit',
        'submit':'登录'
        }

url = 'https://account.ccnu.edu.cn/cas/login;jsessionid=' + cookie
r = requests.post(url,data=payload)
#print(r.text)

sc = r.headers.get('Set-Cookie') or ""
if "CASTGC" in sc:
    print('已成功登录')
else:
    print('未登录成功')
