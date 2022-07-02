# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: ScheduledTask.py
@time: 2022/5/26 20:05
"""
# 定时任务，只能用于电脑一直运行时用
import request
import time
from InterfaceCall import Daily
while True:

    now_hour = time.strftime("%H", time.localtime())

    now_min = time.strftime("%M", time.localtime())

    if now_hour < "10":

        rest = 10 - int(now_hour)

        sleeptime = (rest - 1) * 3600 + (60 - int(now_min)) * 60

        print("启动时北京时间为：" + time.strftime("%H:%M", time.localtime()), "\t软件将在", rest - 1, "小时",
              int((sleeptime - (rest - 1) * 3600) / 60), "分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour > "10":
        rest = 10 - int(now_hour) + 24
        sleeptime = (rest - 1) * 3600 + (60 - int(now_min)) * 60
        print("启动时北京时间为：" + time.strftime("%H:%M", time.localtime()), "\t软件将在", rest - 1, "小时",
              int((sleeptime - (rest - 1) * 3600) / 60), "分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour == "10":
        print("启动时北京时间为：" + time.strftime("%H:%M", time.localtime()), "\t软件将在每天10点发送数据！")
# 以下为定时任务
        Daily.send()
        time.sleep(36000 - int(now_min) * 60)
