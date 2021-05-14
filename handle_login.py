# 使用本地tor代理 9050端口

import requests
from scrapy import Selector

base_url = 'http://xxxxxxxxxs6qbnahsbvxbghsnqh4rj6whbyblqtnmetf7vell2fmxmad.onion/'
proxy = {'http': 'socks5h:127.0.0.1:9050'}
# 账号用户名和密码
username = 'username'
password = 'password'

login_url = base_url + 'entrance/login.php'
index_url = base_url + "entrance/logins.php"

session = requests.session()
session.proxies = proxy


def get_chapter():
    res = session.get(login_url)
    selector = Selector(res)
    img_url = selector.xpath('//img/@src').get()
    with open('./chapter.png', 'wb') as f:
        f.write(session.get(img_url).content)


def login():
    code = input("请输入验证码:")
    post_data = {
        "lgid": username,
        "lgpass": password,
        "sub_code": code,
        "lgsub": "进入系统"
    }
    login_session = session.post(index_url, data=post_data)
    while login_session.url == login_url:
        login()
    print("登录成功")


get_chapter()
login()
