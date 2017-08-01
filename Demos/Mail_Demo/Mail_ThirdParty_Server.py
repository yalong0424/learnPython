#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def sendMail():
    sender = "XXXXXX@qq.com" # 发件人邮箱账号
    password = "XXXXXX" # 发件人邮箱密码
    receiver = "XXXXXX@126.com" # 收件人邮箱账号
    try:
        content = "Python SMTP Email Test"
        msg = MIMEText(content, "plain", "utf-8")
        msg["From"] = formataddr(["yalong", sender]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg["To"] = formataddr(["FK", receiver]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg["Subject"] = "菜鸟教程发送邮件测试"

        server = "smtp.qq.com" #qq邮箱服务器
        port = 465 #qq邮箱端口号
        smtp = smtplib.SMTP_SSL(server, port)
        smtp.login(sender, password) # 括号中对应的是发件人邮箱账号、邮箱密码
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit() # 关闭连接
        print("email send success")
    except smtplib.SMTPException, e:
        print(e)
        print("email send fail")

if __name__ == "__main__":
    sendMail()