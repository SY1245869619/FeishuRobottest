# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: Weekly.py
@time: 2022/6/2 13:25
"""
# 发送周报提醒

import requests
import json


# 在这里改周报的文案
def weekly_time():
    Weekly_Time = "技术周报：6月27日-7月1日"
    return Weekly_Time


# 在这里改周报的链接
def weekly_link():
    Weekly_Link = "https://fangxiang-tech.feishu.cn/docs/doccnT2pE61dAnROLpjJyEzIlwg"
    return Weekly_Link


def get_data():
    data = {
        "msg_type": "interactive",
        "card": {
            "elements": [{
                "tag": "div",
                "text": {
                    "content": "技术周报地址：[" + weekly_time() + "](" + weekly_link() + ")    <at id=all></at>"
                    ,
                    "tag": "lark_md"
                },

            },
                {
                    "tag": "img",
                    "img_key": "img_v2_048ec457-b00b-47d1-bd64-65dae0c154ag",
                    "alt": {
                        "tag": "plain_text",
                        "content": "图片"
                    }
                },
                {
                "actions": [{
                    "tag": "button",
                    "text": {
                        "content": "去完成周报",
                        "tag": "lark_md"
                    },
                    "url": weekly_link(),
                    "type": "default",
                    "value": {}
                }],
                "tag": "action"
            }],
            "header": {
                "title": {
                    "content": "📢 本周技术周报通知",
                    "tag": "plain_text"
                }
            }
        }
    }
    return json.dumps(data, ensure_ascii=True).encode("utf-8")


def req(data):
    # 研发中心群
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/e2e226c4-e953-4740-9c5a-f94e7bf1a7d7"
    # # 消息记录群
    # url = "https://open.feishu.cn/open-apis/bot/v2/hook/f0db5b1a-0ac0-493b-9f86-b6904f2c99a0"
    # url = "https://open.feishu.cn/open-apis/bot/v2/hook/a53dfe87-defb-46b2-bc9a-888e9b56eb1a"
    header = {
        "Content-type": "application/json",
        "charset": "utf-8"
    }
    response = requests.post(url, data=data, headers=header).json()
    print(response)


if __name__ == '__main__':
    req(get_data())