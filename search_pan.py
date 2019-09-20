from urllib import parse

import requests
from bs4 import BeautifulSoup

word = input('搜索内容：')
word = parse.quote(word.encode('gb2312'))
url = 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=' + word
r = requests.get(url)
r.encoding = 'gb2312'
soup = BeautifulSoup(r.text,'html.parser')
answers = soup.find_all('dd')
for tag in answers:
    for part in tag:
        start = part.find('pan.baidu.com')
#        print('*'+ str(start))
        if start != None and start != -1:
            result = part[start:]
            print(result)
