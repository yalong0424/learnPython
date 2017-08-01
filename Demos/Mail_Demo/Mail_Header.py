#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from utils import MailServer

def sendEMail():
    sender = "jiming.wang@mediatek.com"
    receivers = ["jiming.wang@mediatek.com", "fengping.yu@mediatek.com"]

    message = MIMEText("Python 邮件发送测试", "plain", "utf-8")
    message["From"] = Header("菜鸟教程", "utf-8")
    message["To"] = Header("测试", "utf-8")
    message["CC"] = Header("需求", "utf-8")
    subject = "Python SMTP 邮件测试"
    message["Subject"] = Header(subject, "utf-8")

    try:
        smtp = smtplib.SMTP(MailServer.SERVER)
        smtp.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        print("Error: 无法发送邮件。")

if __name__ == "__main__":
    sendEMail()