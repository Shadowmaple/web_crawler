#!/usr/bin/python3

import re
import time

import requests


def crawler():
    url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg"

    querystring = {
        "g_tk":"5381",
        "loginUin":"1142319190",
        "hostUin":"0","format":"json",
        "inCharset":"utf8",
        "outCharset":"GB2312",
        "notice":"0",
        "platform":"yqq.json",
        "needNewCode":"0",
        "cid":"205360772",
        "reqtype":"2",
        "biztype":"1",
        "topid":"237773700",
        "cmd":"8",
        "needmusiccrit":"0",
        "pagenum":"0",
        "pagesize":"25",
        "lasthotcommentid":"",
        "domain":"qq.com",
        "ct":"24",
        "cv":"10101010"
    }

    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Referer': "https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html",
        'Origin': "https://y.qq.com",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'Sec-Fetch-Mode': "cors",
        'Cache-Control': "no-cache",
        'Postman-Token': "8bc11ab4-52e0-4b79-b6ff-dd0e6cebe102,bbeebe82-7a1e-490d-9008-0ef47d31a2a8",
        'Host': "c.y.qq.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    last_comment_id = ""
    files = open("data.txt", "a", encoding = "utf-8")
    count = 0

    # 页码，每页25条评论
    for i in range(2000):
        querystring["pagenum"] = str(i)
        querystring["lasthotcommentid"] = last_comment_id
        response = requests.request("GET", url, headers = headers, params = querystring)

        json_data = response.json()
        if not json_data:
            return None

        comment_list = json_data.get("comment").get("commentlist")
        last_comment_id = comment_list[24].get("commentid")

        # 获取评论，并写入文件
        for comment in comment_list:
            content = comment.get("rootcommentcontent")
            c = re.compile(r'\[em].*[/em].', re.S)
            content = re.sub(c, '', content)
            files.write(content + '\n')
            print("正在写入评论：" + content)
            count += 1

    files.close()
    print("共"+ str(count) + "项评论")

    # return response


if __name__ == '__main__':
    start = time.time()
    # 爬取数据
    crawler()
    end = time.time()
    runtime = end - start
    if runtime <= 60:
        print('Running time: {} Seconds.'.format(runtime))
    else:
        print('Running time: {} Minutes.'.format(runtime / 60))

    print("OK")
