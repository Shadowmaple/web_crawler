import requests
from bs4 import BeautifulSoup as bs


def data():
    url = 'http://www.weather.com.cn/weather1d/101200101.shtml'
    r = requests.get(url)
    r.encoding = "gbk2312"
    soup = bs(r.text, 'html.parser')
    div = soup.find_all('ul','clearfix')
    part = div[1].find('p','wea')
    value = part.get('title')

    weather = {}
    weather['weather'] = value
    return weather

print(data())
