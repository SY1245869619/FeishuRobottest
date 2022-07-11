# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: RecallDaily.py
@time: 2022/6/8 10:32
"""
# 撤回消息
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests

# 获取腾讯token
from Obtain import GetTenantToken
Token = GetTenantToken.GetTenantToken()
TenantToken = 'Bearer ' + str(Token)
print(TenantToken)

# 撤回机器人发送的消息
headers = {
    "Authorization": TenantToken
}
message_id = "om_177dd4b47829c4e3c7807c80f8b886af"

url = "https://open.feishu.cn/open-apis/im/v1/messages/" + message_id

response = requests.request("DELETE", headers=headers, url=url).json()
print(response)
