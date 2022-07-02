# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: test.py
@time: 2022/6/6 10:37
"""
# 调用基本模板
import requests

header = {
    "Content-type": "application/json",
    "charset": "utf-8"
}
data = {
    "ces"
}

url = "https://open.feishu.cn/open-apis/bot/v2/hook/a53dfe87-defb-46b2-bc9a-888e9b56eb1a"

response = requests.request("get", headers=header, data=data, url=url).json()
print(response)
