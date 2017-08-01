#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils import MailServer

class Mail_Base(object):
    def __init__(self):
        self.msg_root = MIMEMultipart()


    def setFromAddress(self, fromAddr):
        self.msg_root["from"] = fromAddr

    def setToAddress(self, toAddrList):
        self.msg_root["to"] = ",".join(toAddrList)

    def setCCAddress(self, ccAddrList):
        self.msg_root["cc"] = ",".join(ccAddrList)

    def setSubject(self, subject):
        self.msg_root["subject"] = subject

    def addPlainText(self, text):
        """
        添加邮件正文内容
        """
        content = MIMEText(text, "plain", "utf-8")
        self.msg_root.attach(content)

    def addHtmlText(self, html):
        """添加HTML格式邮件正文"""
        content = MIMEText(html, "html", "utf-8")
        self.msg_root.attach(content)

    def sendMail(self):
        try:
            smtp = smtplib.SMTP(MailServer.SERVER)
            smtp.sendmail(self.msg_root["from"], self.msg_root["to"], self.msg_root.as_string())
            print("email send success")
        except smtplib.SMTPException, e:
            print(e)
            print("email send fail")