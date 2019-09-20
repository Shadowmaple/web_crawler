# 通过视频api获取视频号和标题

import requests

url = 'https://www.bilibili.com/index/ding.json'
json = requests.get(url).json()
douga = json.get('douga')
for i in range(10):
    av = str(douga[str(i)]['aid'])
    title = douga[str(i)]['title']
    print('av:'+ av + '   '+ title)
