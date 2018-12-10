import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.qidian.com/rank/pubnewbook'
r = requests.get(url)
soup = bs(r.text,'html.parser')
part = soup.find_all('div', 'book-mid-info')
sum = 0
for tag in part:
    x = tag.find('a')
    print(x.text)
    sum += 1
print('#共' + str(sum) + '个项目#')
