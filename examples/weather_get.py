"""参考:https://zhuanlan.zhihu.com/p/26369491"""

def weather():
    import requests
    r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
    r.encoding='utf-8'
    print(r.json()['weatherinfo']['city'], 
            r.json()['weatherinfo']['WD'], 
            r.json()['weatherinfo']['temp'])

if __name__=='__main__':
    weather()

