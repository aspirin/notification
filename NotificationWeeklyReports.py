
import json

import requests


def dingmessage():
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=a2ca931da90062f5ab23497026c45d87695bf5ddda1098d545e690e390b2ff89"
    #构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    #构建请求数据
    tex = "周报提交提醒"
    message ={
        "msgtype": "markdown",
        "markdown": {
            "title": tex,
            "text": "#### 周报提交提醒 @all \n> 请大家到[钉钉知识库-》技术部共享库-》团队周报](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fnotes.dingtalk.com%2Fnotes%2FO5pXBjOQyEBQX7Zv%3ForgId%3D86201021%26ddtab%3Dtrue%26dd_progress%3Dfalse%26showmenu%3Dfalse) 中提交周报，如已提交，请忽略! \n> ###### By 简账钉钉机器人 \n"
        },
        "at": {
            "isAtAll": True
        }
    }
    #对请求的数据进行json封装
    message_json = json.dumps(message)
    #发送请求
    info = requests.post(url=webhook,data=message_json,headers=header)
    #打印返回的结果
    print(info.text)
if __name__=="__main__":
    dingmessage()