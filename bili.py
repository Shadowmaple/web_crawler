import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.bilibili.com/v/douga/?spm_id_from=333.5.b_7072696d6172795f6d656e75.2'
r = requests.get(url)
soup = bs(r.text,'lxml')
answers = soup.find_all('div',class_="spread-module")
print(answers)
for tag in answers:
    print('&')
    tag_ = tag.find('p', "t")
    title = tag_.text
    print(title)
