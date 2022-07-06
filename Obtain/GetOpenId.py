# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetOpenId.py
@time: 2022/5/26 19:25
"""
# 获取每个人的openid,方便@人
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests
from Obtain import GetTenantToken

Token = GetTenantToken.GetTenantToken()
TenantToken = 'Bearer ' + str(Token)
print(TenantToken)

headers = {
    'Authorization': TenantToken,
    'Content-Type': '"application/json; charset=utf-8"'
}

data = {
    "emails": [
        "1245869619@qq.com", "luoheng@kachexiongdi.com"
    ],
    "mobiles": [
        "17713146220", "15827285750"
    ],

}
url = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id"

res = requests.post(url=url, headers=headers, json=data).json()
print(res)
