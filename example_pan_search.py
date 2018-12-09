# coding; utf-8
import requests
from bs4 import BeautifulSoup
import urllib

target = input('搜索内容: ')
target = urllib.parse.quote(target.encode('gb2312'))
url = 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=' + target

def get_url():
    html = requests.get(url)
    html.encoding = 'gb2312'
    html = html.text
    soup = BeautifulSoup(html, "html.parser")
    answers = soup.find_all('dd', 'dd answer')
    for tag in answers:
        for part in tag.contents:
            start = part.find('pan.baidu.com')
            if (start != None and start != -1):
                pan = part[start:]
                print(pan)
        

if __name__ == '__main__':
    get_url()
