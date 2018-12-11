import requests
from bs4 import BeautifulSoup as bs
from urllib import parse

def search(name):
    url = 'https://www.qidian.com/search?kw=' + name
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    tag = soup.find_all('div', 'book-mid-info')
    flag = False
    for part in tag:
        title = part.find('a').text
        if (name in title):
            print('\n'+ title)
            intro = part.find('p','intro').text
            print('   '+intro.strip()+ '……')
            flag = True
    if not flag:
        print('起点太垃圾了，连这本书都没有！')

if __name__ == '__main__':
    name = input('搜索书名：')
    search(name)
