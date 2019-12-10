import requests

url = "https://accounts.douban.com/j/mobile/login/basic"

username = ""
pwd = "***"

payload = "ck=03PG&name=" + username + "&password=" + pwd + "&remember=false&ticket="
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
    'Content-Type': "application/x-www-form-urlencoded",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
