# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: Daily.py
@time: 2022/5/26 17:11
"""
# 飞书机器人发送消息
# 保证程序运行时，控制台能够搜索路径时能够调用自己写的module
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import requests
import json
from Obtain import GetTenantToken
from Resources import DailyContent, weather
import time


def send():
    # 消息卡片内容
    msgContent = {
        # 消息卡片头消息
        "header": DailyContent.headerMSG(),
        "i18n_elements": {
            "zh_cn": [
                # 消息卡片图片消息
                DailyContent.imgMSG(),
                {
                    "tag": "div",
                    "text": {
                        # 消息卡片项目提醒内容消息
                        "content": DailyContent.contentMSG1(),
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "tag": "markdown",
                    # 消息卡片需求进展内容消息
                    "content": DailyContent.contentMSG2()
                },
                # 消息卡片按钮
                DailyContent.buttonMSG(),
                {
                    "tag": "hr"
                },
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": weather.weather()
                    }
                }

            ]
        }
    }

    # 请求体
    req = {
        # # 消息记录群（测试）
        "receive_id": "oc_dc684ab9c57e6d7ba42330ac2a293603",
        # 产品研发群
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
    print("Daily腾讯Token拼接               "+TenantToken)

    # 请求头
    headers = {
        'Authorization': TenantToken,
        "Content-type": "application/json; charset=utf-8"
    }

    # 链接地址
    url = "https://open.feishu.cn/open-apis/im/v1/messages"

    # 发起请求，并将返回数据打印
    response = requests.request("POST", url, params=params, headers=headers, data=data).json()
    # 打印返回数据的content数据
    print("Daily返回数据打印              ")
    print(response)
    # 取出返回数据的message_id数据
    message_id = response["data"]["message_id"]
    # 不覆盖的将message_id数据写在txt文件中
    with open('../Resources/message_id_log.txt', 'a') as f:  # 设置文件对象
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()) + "\n" + "message_id:" + message_id, file=f)


if __name__ == '__main__':
    send()
