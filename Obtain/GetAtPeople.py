# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetAtPeople.py
@time: 2022/6/7 15:13
"""
import Resources.DailyContent


def atpeople(atp=""):
    word = Resources.DailyContent.atPerson()
    if word.count("沈缘") > 0:
        atp = "<at email=shenyuan@kachexiongdi.com></at>"
    if word.count("罗恒") > 0:
        atp = atp + "<at email=luoheng@kachexiongdi.com></at>"
    if word.count("王帆") > 0:
        atp = atp + "<at email=wangfan@kachexiongdi.com></at>"
    if word.count("陈可伊") > 0:
        atp = atp + "<at email=chenkeyi@kachexiongdi.com></at>"
    if word.count("李春立") > 0:
        atp = atp + "<at email=lichunli@kachexiongdi.com></at>"
    if word.count("李太明") > 0:
        atp = atp + "<at email=litaiming@kachexiongdi.com></at>"
    if word.count("刘晶晶") > 0:
        atp = atp + "<at email=liujingjing@kachexiongdi.com></at>"
    if word.count("张颖") > 0:
        atp = atp + "<at email=zhangying@kachexiongdi.com></at>"
    if word.count("田万丰") > 0:
        atp = atp + "<at email=tianwanfeng@kachexiongdi.com></at>"
    if word.count("陈国伟") > 0:
        atp = atp + "<at email=chenguowei@kachexiongdi.com></at>"
    if word.count("韦旭安") > 0:
        atp = atp + "<at email=weixuan@kachexiongdi.com></at>"
    if word.count("陈鹏") > 0:
        atp = atp + "<at email=chenpeng@kachexiongdi.com></at>"
    if word.count("李子朋") > 0:
        atp = atp + "<at email=lizipeng@kachexiongdi.com></at>"
    if word.count("刘清清") > 0:
        atp = atp + "<at email=liuqingqing@kachexiongdi.com></at>"
    if word.count("王彬") > 0:
        atp = atp + "<at email=wangbin@kachexiongdi.com></at>"
    if word.count("吴亦凡") > 0:
        atp = atp + "<at email=wuyifan@kachexiongdi.com></at>"
    if word.count("徐嘉鑫") > 0:
        atp = atp + "<at email=xujiaxin@kachexiongdi.com></at>"
    if word.count("许帅毅") > 0:
        atp = atp + "<at email=xushuaiyi@kachexiongdi.com></at>"
    if word.count("杨季涛") > 0:
        atp = atp + "<at email=yangjitao@kachexiongdi.com></at>"
    if word.count("张红飞") > 0:
        atp = atp + "<at email=zhanghongfei@kachexiongdi.com></at>"
    if word.count("张佳丽") > 0:
        atp = atp + "<at email=zhangjiali@kachexiongdi.com></at>"
    if word.count("张磊峰") > 0:
        atp = atp + "<at email=zhangleifeng@kachexiongdi.com></at>"
    if word.count("张猛") > 0:
        atp = atp + "<at email=zhangmeng@kachexiongdi.com></at>"
    if word.count("王美玲") > 0:
        atp = atp + "<at email=wangmeiling@kachexiongdi.com></at>"
    if word.count("董世昌") > 0:
        atp = atp + "<at email=dongshichang@kachexiongdi.com></at>"
    if word.count("管世昭") > 0:
        atp = atp + "<at email=guanshizhao@kachexiongdi.com></at>"
    if word.count("朱元召") > 0:
        atp = atp + "<at email=zhuyuanzhao@kachexiongdi.com></at>"
    if word.count("徐乃煊") > 0:
        atp = atp + "<at email=xunaixuan@kachexiongdi.com></at>"
    if word.count("王宇飞") > 0:
        atp = atp + "<at email=wangyufei@kachexiongdi.com></at>"
    if word.count("魏峰") > 0:
        atp = atp + "<at email=weifeng@kachexiongdi.com></at>"
    if word.count("程正男") > 0:
        atp = atp + "<at email=chengzhengnan@kachexiongdi.com></at>"
    if word.count("王友忠") > 0:
        atp = atp + "<at email=wangyouzhong@kachexiongdi.com></at>"
    if word.count("王超") > 0:
        atp = atp + "<at email=wangchao@kachexiongdi.com></at>"
    if word.count("高凯") > 0:
        atp = atp + "<at email=gaokai@kachexiongdi.com></at>"
    if word.count("郑清源") > 0:
        atp = atp + "<at email=zhengqingyuan@kachexiongdi.com></at>"
    if word.count("王婷亚") > 0:
        atp = atp + "<at email=wangtingya@kachexiongdi.com></at>"
    if word.count("贾晓然") > 0:
        atp = atp + "<at email=jiaxiaoran@kachexiongdi.com></at>"
    else:
        print("退出@邮箱检索")
    return atp
