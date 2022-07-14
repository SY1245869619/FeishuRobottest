# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: DailyContent.py
@time: 2022/6/6 16:36
"""
# 日报消息卡片内容配置
import sys
import os

# 这些是可以引用其他文件夹的前提，一定不要动，不要改位置
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import datetime
from Obtain import GetAtPeople


# 日报消息内容资源，当前日期
def time():
    Ti = datetime.date.today()
    Me = str(Ti)
    return Me


# 项目缺陷及会议提醒（固定）
def contentMSG1():
    content_msg1 = "***项目缺陷及会议提醒***" \
                   "\n" \
                   + bugMSG1() + \
                   "\n\n" \
                   + bugMSG2() + \
                   "\n\n" \
                   + bugMSG3() + \
                   "\n\n" \
                   + bugMSG4()
    return content_msg1


# 消息标题头配置（固定）
def headerMSG():
    header_msg = {
        "template": "turquoise",
        "title": {
            # 基本固定不变的标题
            "content": "📚每日项目情况汇报    🕐" + time(),
            "tag": "plain_text"
        }
    }
    return header_msg


# 消息中卡片图片配置（固定）
def imgMSG():
    img_msg = {
        "alt": {
            "content": "我们的使命是：打造无界物流，推动物流产业升级,我们的价值观是：坚持，专注，美好,我们的愿景是：成为大宗商品物流行业领先的物流科技公司",
            "tag": "plain_text"
        },
        # 更改img_key的值，可以更换照片，需提前上传图片
        "img_key": "img_v2_048ec457-b00b-47d1-bd64-65dae0c154ag",
        "tag": "img"
    }
    return img_msg


# 禅道BUG提醒配置（经常变）
def bugMSG1():
    bug_msg1 = "**一、禅道BUG提醒**" \
               "\n" \
               "未关闭项目BUG总数***52个***(网络货运项目)" \
               "\n" \
               + GetAtPeople.atpeople()
    return bug_msg1


# 配置@人（经常变）
def atPerson():
    at_person = ["董世昌", "王彬", "李子朋", "杨季涛", "徐嘉鑫", "韦旭安", "管世昭", "李春立", "罗恒", "吴亦凡", "陈鹏", "张佳丽"]
    return at_person


# 产品需求文档配置（经常变）
def bugMSG2():
    bug_msg2 = "**二、产品需求文档**" \
               "\n" \
               "[路桥项目产品整体需求文档](https://fangxiang-tech.feishu.cn/docs/doccnvC3mxf04H5nddyBCQ2Gdvg)" \
               "\n" \
               "[灵石订单的自动审核-方案](https://fangxiang-tech.feishu.cn/docx/doxcndBCNP5k564OvLrpMHqQkFg)" \
               "\n" \
               "[7.6日矿大需求-增加实时审批节点以及数据安全问题解决](https://fangxiang-tech.feishu.cn/docx/doxcnf0B0N0yARMJfyx0wZCA5af)"\
               "\n" \
               "[电子合同需求](https://fangxiang-tech.feishu.cn/docx/doxcnHhIO3an3p9OVdIc59UIg4b)"\
               "\n" \
               "[自有车校验需求](https://fangxiang-tech.feishu.cn/docx/doxcnizwASDRSyGFAJKUy2UpQjg)"\
               "\n" \
               "[7.13灵石项目需求-新增治超办角色相关功能](https://fangxiang-tech.feishu.cn/docx/doxcnpyTitGJcHsOyxvKalCMO4c?from" \
               "=auth_notice&hash=ae5b93e27c11c02bef0765700421056e) "
    return bug_msg2


# 上线时间配置（固定）
def bugMSG3():
    bug_msg3 = "**三、上线时间**" \
               "\n" \
               "排期文档：" \
               "[项目排期](https://fangxiang-tech.feishu.cn/sheets/shtcnfnAtZnTTU1iDQCG3GKPcid)"
    return bug_msg3


# 需求评审会议配置（暂时固定）
def bugMSG4():
    bug_msg4 = "**四、需求评审会议**" \
               "\n" \
               "提前一天说，暂时未知"
    return bug_msg4


# 需求进展情况汇报（经常变）
def contentMSG2():
    content_msg2 = "***需求进展情况汇报***" \
                   "\n" \
                   "**电子合同需求[🗂️](https://fangxiang-tech.feishu.cn/docs/doccnW2nDLTy2rOW3UoQC6HyuBb)**" \
                   "\n" \
                   "产品: Android&iOS司机端、货主端" \
                   "\n" \
                   "产品：SaaS+运营后台，平台与交易多方签订电子协议" \
                   "\n" \
                   "说明：进行中" \
                   "\n" \
                   "**路桥整体需求[🗂️](https://fangxiang-tech.feishu.cn/docs/doccnvC3mxf04H5nddyBCQ2Gdvg)**" \
                   "\n" \
                   "产品: 路桥项目-白名单优化(结算流程和开票流程)" \
                   "\n" \
                   "产品: 路桥项目-需求104-SaaS及h5部分服务费" \
                   "\n" \
                   "产品: 路桥项目-货源信息审核及其他功能优化-SaaS部分" \
                   "\n" \
                   "产品: 路桥项目-框架协议优化-SaaS部分" \
                   "\n" \
                   "产品: 路桥项目-框架协议优化-司机端" \
                   "\n" \
                   "产品: 路桥项目-框架协议优化-货主端" \
                   "\n" \
                   "产品: 路桥项目-货源信息审核-货主端（iOS）" \
                   "\n" \
                   "说明：进行中" \
                   "\n" \
                   "**后台优化需求**" \
                   "\n" \
                   "产品: 方向云，运营平台，sass异步任务队列拆分" \
                   "\n" \
                   "说明：进行中" \
                   "\n" \
                   "**灵石项目需求**" \
                   "\n" \
                   "产品: 灵石项目需求-新增治超办角色相关功能" \
                   "\n" \
                   "说明：进行中" \
                   "\n" \
                   "<at id=all></at>"
    return content_msg2


# 消息卡片按钮配置（固定）
def buttonMSG():
    button_msg = {
        "tag": "action",
        "actions": [
            {
                "tag": "button",
                "text": {
                    "tag": "plain_text",
                    "content": "👀去禅道查看"
                },
                "multi_url": {
                    "url": "http://zentao.kachexiongdi.com/biz/my/",
                    "android_url": "http://zentao.kachexiongdi.com/biz/my/",
                    "ios_url": "http://zentao.kachexiongdi.com/biz/my/",
                    "pc_url": "http://zentao.kachexiongdi.com/biz/my/"
                },
                "type": "primary"
            },
            {
                "tag": "button",
                "text": {
                    "tag": "plain_text",
                    "content": "📝去云文档查看"
                },
                "multi_url": {
                    "url": "https://fangxiang-tech.feishu.cn/drive/folder/fldcnCFjx2vkfKYG5U5eefKStrg"
                           "?from=space_persnoal_filelist",
                    "android_url": "https://fangxiang-tech.feishu.cn/drive/folder"
                                   "/fldcnCFjx2vkfKYG5U5eefKStrg?from=space_persnoal_filelist",
                    "ios_url": "https://fangxiang-tech.feishu.cn/drive/folder/fldcnCFjx2vkfKYG5U5eefKStrg"
                               "?from=space_persnoal_filelist",
                    "pc_url": "https://fangxiang-tech.feishu.cn/drive/folder/fldcnCFjx2vkfKYG5U5eefKStrg"
                              "?from=space_persnoal_filelist "
                },
                "type": "primary"
            }
        ]
    }
    return button_msg
