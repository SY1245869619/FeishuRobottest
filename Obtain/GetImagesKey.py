# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetImagesKey.py
@time: 2022/6/6 14:52
"""
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import GetTenantToken
import requests
from requests_toolbelt import MultipartEncoder

Token = GetTenantToken.GetTenantToken()
TenantToken = 'Bearer ' + str(Token)
print(TenantToken)

data = {
    "image_type": "message",
    # 'image': (open('../Resources/image.png', 'rb'))
    'image': (open('../Resources/weekly1.jpg', 'rb'))

}

multi_data = MultipartEncoder(data)

header = {
    "Authorization": TenantToken,
    "Content-Type": multi_data.content_type
}

url = "https://open.feishu.cn/open-apis/im/v1/images"

response = requests.request("post", headers=header, data=multi_data, url=url).json()
print(response)
# image_key
# image.png
# img_v2_048ec457-b00b-47d1-bd64-65dae0c154ag
# weekly1.jpg
# img_v2_fca2a46e-9ff1-4ad7-894a-05b4fa7a369g
