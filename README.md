---
title: python简单的邮箱报警脚本
tags:
 - mail
categories: python
---

>首先配置邮箱
```python
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
config_info = {
    "To": ["12345678@qq.com"],
    'From': "igreedy@163.com",
    'Subject': "分析日志监控到异常".decode('UTF-8'),
    'Smtpserver': "smtp.163.com",
    'Username': "igreedy@163.com",
    'Password': ""
}
```
>其中值得注意的是Smtpserver，如果你用来发送的是163邮箱，那么它就是smtp.163.com。
但如果是其他的。例如qq邮箱就是 smtp.exmail.qq.com。

```python
if __name__ == '__main__':
    try:
        print 1/0
    except Exception as e:
        group = {"data_path": os.path.realpath(__file__), "status": "successful", "error": ""}
        group["error"] = str(e)
        group["status"] = "failed"
        mail_notify(json.dumps(group, indent=4))
        raise
```
>只要包裹try/except，里面添加邮箱提醒代码就ok了，里面用到了mail.py的类对象。
执行python demo.py,会接收到的邮箱内容如下：
```
{
    "status": "failed",
    "data_path": "/home/mail_notify/demo.py",
    "error": "integer division or modulo by zero"
}

docker0   Link encap:Ethernet  HWaddr 02:42:d6:bb:30:ba
    inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
    UP BROADCAST MULTICAST  MTU:1500  Metric:1
    RX packets:0 errors:0 dropped:0 overruns:0 frame:0
    TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
    collisions:0 txqueuelen:0
    RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```









