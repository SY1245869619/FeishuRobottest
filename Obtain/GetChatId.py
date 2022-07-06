# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetChatId.py
@time: 2022/5/31 18:36
"""
# 获取群组chat_id
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import GetTenantToken
import requests

Token = GetTenantToken.GetTenantToken()
TenantToken = 'Bearer ' + str(Token)
print(TenantToken)
headers = {
    "Authorization": TenantToken,
    "Content-Type": "application/json; charset=utf-8"
}
url = "https://open.feishu.cn/open-apis/im/v1/chats"
response = requests.request("get", headers=headers, url=url).json()
# print(response)

# 'chat_id': 'oc_a8ca381b96903c22e046faea1082f3f8',
# 'name': '产品研发',
# 'tenant_key': '13f3b5f8adcfd747'
# 'chat_id': 'oc_dc684ab9c57e6d7ba42330ac2a293603',
# 'name': '消息记录群',
# 'tenant_key': '13f3b5f8adcfd747'
