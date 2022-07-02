# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: RecallDaily.py
@time: 2022/6/8 10:32
"""
# 撤回消息

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
message_id = "om_34e0ee240ab95d269d81daf928ffc31c"

url = "https://open.feishu.cn/open-apis/im/v1/messages/" + message_id

response = requests.request("DELETE", headers=headers, url=url).json()
print(response)
