#!/usr/bin/python
# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from utils import MailServer
import Mail_Multi_Base

class Mail(Mail_Multi_Base.Mail_Base):
    def __init__(self):
        super(Mail, self).__init__()

    def addAttachFiles(self, files):
        """
        构造附件
        """
        for file in files:
            att = MIMEText(open(file, "rb").read(), "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            file_name = file[file.rfind(r"/") + 1: ]
            att["Content-Disposition"] = "attachment;filename=%s"%file_name
            self.msg_root.attach(att)

def sendMail():
    mail = Mail()
    mail.setFromAddress(MailServer.FROM)
    mail.setToAddress(MailServer.To)
    mail.setCCAddress(MailServer.CC)
    subject = "pyhton smpt attachment test"
    mail.setSubject(subject)

    #设置邮件正文内容
    #content = "Python 附件测试"
    #mail.addPlainText(content)
    content = open("./Html/DailyReminder.html").read()
    mail.addHtmlText(content)
    #添加附件
    attach_files = ["./Html/DailyReminder.html", "./Html/LogTimeWeeklyReport.html",
                    "./Html/AfternoonReminderHttp.rar", "./Html/DailyReminder.zip"]
    mail.addAttachFiles(attach_files)
    mail.sendMail()

if __name__ == "__main__":
    sendMail()