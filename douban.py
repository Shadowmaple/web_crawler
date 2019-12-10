import requests

url = "https://accounts.douban.com/j/mobile/login/basic"

payload = "ck=03PG&name=1142319190%40qq.com&password=douban768830&remember=false&ticket="
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
    'Content-Type': "application/x-www-form-urlencoded",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
