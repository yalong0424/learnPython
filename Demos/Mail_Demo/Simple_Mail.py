#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from utils import MailServer

class Mail(object):
    def __init__(self):
        self.__msg_root = MIMEText("Python 发送邮件测试", "plain", "utf-8")

    def fromAddress(self, fromAddr):
        self.__msg_root["from"] = fromAddr

    def toAddress(self, toAddr):
        self.__msg_root["to"] = ",".join(toAddr)

    def ccAddr(self, ccAddr):
        self.__msg_root["cc"] = ",".join(ccAddr)

    def subject(self, subject):
        self.__msg_root["subject"] = Header(subject, "utf-8")

    def sendMail(self):
        smtp = smtplib.SMTP(MailServer.SERVER)
        smtp.sendmail(self.__msg_root["from"], self.__msg_root["to"], self.__msg_root.as_string())

def sendMail():
    sender = "jiming.wang@mediatek.com"
    receivers = ["jiming.wang@mediatek.com"]
    cc = ['jiming.wang@mediatek.com']
    subject = "Python SMTP Test"

    mail = Mail.Mail()
    mail.fromAddress(sender)
    mail.toAddress(receivers)
    mail.ccAddr(cc)
    mail.subject(subject)
    mail.sendMail()

if __name__ == "__main__":
    sendMail()