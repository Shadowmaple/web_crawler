import requests
from bs4 import BeautifulSoup as bs
import qidian_search as sr

def new():
    url = 'https://www.qidian.com/rank/pubnewbook'
    r = requests.get(url)
    soup = bs(r.text,'html.parser')
    part = soup.find_all('div', 'book-mid-info')
    sum = 0
    for tag in part:
        x = tag.find('a')
        print(x.text)
        sum += 1
    print('----------')
    print('#共' + str(sum) + '个项目')

def finish():
    url = 'https://www.qidian.com/finish'
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    tag = soup.find_all('div', 'book-mid-info')
    sum = 0
    for part in tag:
        title = part.find('a').text
        print(title)
        sum += 1
    print('----------')
    print('#共'+str(sum)+'个项目')


key = input('关键字：')
if (key=='新书'):
    new()
elif (key=='完本'):
    finish()
else:
    sr.search(key)
