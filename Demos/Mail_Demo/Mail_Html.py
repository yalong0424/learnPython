#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from utils import MailServer

def sendHtmlMail(html_msg):
    msg_root = MIMEText(html_msg, "html", "utf-8")
    msg_root["From"] = MailServer.FROM
    msg_root["To"] = ",".join(MailServer.To)
    msg_root["CC"] = ",".join(MailServer.CC)

    subject = "Python SMTP HTML邮件测试"
    msg_root["Subject"] = Header(subject, "utf-8")

    try:
        smtp = smtplib.SMTP(MailServer.SERVER)
        smtp.sendmail(msg_root["From"], msg_root["To"], msg_root.as_string())
        print("email send successed")
    except smtplib.SMTPException, e:
        print(e)

def sendHtml():
    msg_html = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.runoob.com">这是runoob链接</a></p>
        """
    sendHtmlMail(msg_html)

def sendHtmlFile():
    file_name = "./Html/LogTimeWeeklyReport.html"
    message = open(file_name).read()
    sendHtmlMail(message)

if __name__ == "__main__":
    sendHtml()
    sendHtmlFile()