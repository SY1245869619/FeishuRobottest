# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetTenantToken.py
@time: 2022/5/31 14:29
"""
# 获取腾讯Token
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests


def GetTenantToken():
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    params = {
        # 企业自建应用的app_id和app_secret
        "app_id": "cli_a20587a031e5100d",
        "app_secret": "DyrdFJXlddhVN9GG8QcxjbRcaz4Y7vCy"
    }
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"

    response = requests.request("POST", url, headers=headers, params=params)
    # print(response.content)
    TenantToken = response.json()['tenant_access_token']
    # print(TenantToken)
    return TenantToken


if __name__ == '__main__':
    GetTenantToken()
