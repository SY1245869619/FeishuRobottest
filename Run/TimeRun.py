# -*- coding: UTF-8 -*-
'''
@Project ：test2.py 
@File    ：TimeRun.py
@IDE     ：PyCharm 
@Author  ：萌新小缘
@Date    ：2022/7/2 18:48 
'''

import requests
import time
from InterfaceCall import Weekly, Daily


def timeRun():
    # 自行设置格式 格式20211224
    nowTime = time.strftime('%Y%m%d', time.localtime())
    # 节假日接口(工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2 )
    server_url = "https://api.apihubs.cn/holiday/get?cn=1&size=31&date=" + nowTime
    req = requests.get(server_url).json()
    # print(req)
    # 获取data值
    # 判断是否为工作日
    workday = req['data']['list'][0]['workday']
    # 星期几
    week_cn = req['data']['list'][0]['week_cn']
    # 是否为工作日
    workday_cn = req['data']['list'][0]['workday_cn']
    # 法定节假日判断
    holiday_legal_cn = req['data']['list'][0]['holiday_legal_cn']
    # print('日期 ' + str(nowTime) + '\n查询结果为 ' + str(workday_cn) + '\n结论 ', end=' ')
    # 这个用来判断节假日放假什么的
    if holiday_legal_cn == '法定节假日':
        print('TimeRun日期节假日查询➡➡➡               法定节假日')
        Weekly.send()
    elif int(workday) == 1:
        print('TimeRun日期节假日查询➡➡➡                工作日')
        Daily.send()
        if week_cn == '星期五':
            print('TimeRun日期节假日查询➡➡➡                星期五')
            Weekly.send()
    elif int(workday) == 2:
        print('TimeRun日期节假日查询➡➡➡                非工作日')
        Weekly.send()
        Daily.send()
    else:
        print('TimeRun日期节假日查询➡➡➡                Error出错了')


if __name__ == '__main__':
    timeRun()
