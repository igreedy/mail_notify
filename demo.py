# coding:utf8

from mail import Mail

import os
import json


def mail_notify(msg):
    """
    To    接受者(must)
    Cc    抄送(option)
    Bcc   密送(option)
    From  发送者(must)
    Subject 邮件主题
    Smtpserver smtp服务器(must)
    Username  发送用户名(must)
    Password  发送密码(must)
    Sender 发送者(option)
    """
    msg = msg.encode('utf-8')
    config_info = {
        "To": ["12345678@qq.com"],
        'From': "igreedy@163.com",
        'Subject': "分析日志监控到异常".decode('UTF-8'),
        'Smtpserver': "smtp.163.com",
        'Username': "igreedy@163.com",
        'Password': ""
    }
    msg = msg.replace("\n", "<br>").replace(" ", "&nbsp;")
    mail = Mail(config_info)
    mail.add_text(msg)
    mail.add_text("<br><br>")
    ifconfig = os.popen("/sbin/ifconfig").read()
    ifconfig = ifconfig.replace("\n", "<br>").replace(" ", "&nbsp;")
    mail.add_text(ifconfig)
    mail.send()


if __name__ == '__main__':
    try:
        print 1/0
    except Exception as e:
        group = {"data_path": os.path.realpath(__file__), "status": "successful", "error": ""}
        group["error"] = str(e)
        group["status"] = "failed"
        mail_notify(json.dumps(group, indent=4))
        raise
