# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: weather.py
@time: 2022/6/9 10:25
"""
# coding=utf-8
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests


def weather():
    yburl = 'https://free-api.heweather.com/s6/weather/forecast'
    cyurl = 'https://free-api.heweather.com/s6/weather/lifestyle'

    value = {
        'location': '北京',
        'key': 'e63cf40578ea460b9dde42648661be91',
        'lang': 'zh'
    }

    ybreq = requests.get(yburl, params=value)
    cyreq = requests.get(cyurl, params=value)

    ybjs = ybreq.json()
    cyjs = cyreq.json()
    # print(cyjs)

    yb = ybjs['HeWeather6'][0]['daily_forecast']
    cy = cyjs['HeWeather6'][0]['lifestyle'][1]
    gj = cyjs['HeWeather6'][0]['lifestyle'][0]
    gx = cyjs['HeWeather6'][0]['update']
    d1 = u'北京🌏' + '  ' + yb[0]['date'] + ' ' + yb[0]['cond_txt_d']
    d2 = u'北京🌏' + '  ' + yb[1]['date'] + ' ' + yb[1]['cond_txt_d']
    d3 = gj['txt'] + ' ' + cy['txt']
    d4 = d1 + '\n' + d3 + '\n'
    d5 = d2 + '\n' + d3 + '\n'
    d7 = "天气更新时间:" + gx['loc']
    weather_tq = d4 + d5 + d7
    print("weather返回数据打印⬇⬇⬇                \n"+weather_tq)
    return weather_tq


if __name__ == '__main__':
    weather()
