# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: request.py
@time: 2022/5/26 17:11
"""
# 请求测试
# 飞书机器人发送消息
import requests
import json
from Obtain import GetTenantToken
from Resources import DailyContent


def send():
    msgContent = {
        "header": DailyContent.headerMSG(),
        "i18n_elements": {
            "zh_cn": [
                DailyContent.imgMSG(),
                {
                    "tag": "div",
                    "text": {
                        "content": DailyContent.contentMSG1(),
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "tag": "markdown",
                    "content": DailyContent.contentMSG2()
                },
                DailyContent.buttonMSG()
            ]
        }
    }

    # 请求体
    req = {
        # 消息记录群（测试）
        "receive_id": "oc_dc684ab9c57e6d7ba42330ac2a293603",
        # # 产品研发群
        # "receive_id": "oc_a8ca381b96903c22e046faea1082f3f8",
        "content": json.dumps(msgContent),
        "msg_type": "interactive",
    }
    data = json.dumps(req)

    # 参数
    params = {"receive_id_type": "chat_id"}

    # 获取腾讯token
    Token = GetTenantToken.GetTenantToken()
    TenantToken = 'Bearer ' + str(Token)
    print(TenantToken)

    # 请求头
    headers = {
        'Authorization': TenantToken,
        "Content-type": "application/json; charset=utf-8"
    }

    # 链接地址
    url = "https://open.feishu.cn/open-apis/im/v1/messages"

    # 发起请求，并将返回数据打印
    response = requests.request("POST", url, params=params, headers=headers, data=data)
    # 打印返回数据的content数据
    print(response.content)


if __name__ == '__main__':
    send()
