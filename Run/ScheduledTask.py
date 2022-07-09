# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: ScheduledTask.py
@time: 2022/5/26 20:05
"""
import sys
import os
# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# 定时任务，只能用于电脑一直运行时用
import time
from Run import TimeRun
while True:
    # 现在的时间
    now_hour = time.strftime("%H", time.localtime())
    # 现在的分钟
    now_min = time.strftime("%M", time.localtime())
    if now_hour < "10":
        rest = 10 - int(now_hour)
        sleeptime = (rest - 1) * 3600 + (60 - int(now_min)) * 60
        print("启动时北京时间为：" + time.strftime("%Y-%m-%d %X", time.localtime()), "\t软件将在", rest - 1, "小时",
              int((sleeptime - (rest - 1) * 3600) / 60), "分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour > "10":
        rest = 10 - int(now_hour) + 24
        sleeptime = (rest - 1) * 3600 + (60 - int(now_min)) * 60
        print("启动时北京时间为：" + time.strftime("%Y-%m-%d %X", time.localtime()), "\t软件将在", rest - 1, "小时",
              int((sleeptime - (rest - 1) * 3600) / 60), "分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour == "10":
        print("启动时北京时间为：" + time.strftime("%Y-%m-%d %X", time.localtime()), "\t软件将在每天10点发送数据！")
        TimeRun.timeRun()
        time.sleep(36000 - int(now_min) * 60)
