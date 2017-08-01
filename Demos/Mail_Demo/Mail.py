#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from utils import MailServer

"""
完整版Mail Demo
"""

class Mail(object):
    def __init__(self):
        self.msg_root = MIMEMultipart("related")
        self.msg_alternative = MIMEMultipart("alternative")
        self.msg_root.attach(self.msg_alternative)
        self.__content = ""

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
        添加邮件正文内容，将普通文本内容追加到HTML格式中进行显示
        """
        self.__content += "<p>%s</p>"%text

    def addHtmlText(self, html):
        """添加HTML格式邮件正文"""
        self.__content += html

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

    def addPictures(self, picture_file_list):
        self.__content += """
        <p>Python Pictures 邮件测试</p>
        <p><a href="http://www.runoob.com">菜鸟教程</a></p>
        <p>图片演示：</p>
        """
        for file in picture_file_list:
            fp = open(file, "rb")
            msg_image = MIMEImage(fp.read())
            fp.close()

            #以图片名作为图片ID
            file_name = file[file.rfind(r"/") + 1: ]
            picture_id = file_name[: file_name.rfind(".")]

            #将图片添加到HTML中
            self.__content += "<p><img src='cid:%s'></p>"%picture_id

            #定义图片ID，在HTML中引用
            msg_image.add_header("Content-ID", "<%s>"%picture_id)
            self.msg_root.attach(msg_image)

    def sendMail(self):
        try:
            # 添加邮件正文
            content = MIMEText(self.__content, "html", "utf-8")
            self.msg_alternative.attach(content)
            smtp = smtplib.SMTP(MailServer.SERVER)
            smtp.sendmail(self.msg_root["from"], self.msg_root["to"], self.msg_root.as_string())
            print("email send success")
        except smtplib.SMTPException, e:
            print(e)
            print("email send fail")

def sendMail():
    mail = Mail()
    mail.setFromAddress(MailServer.FROM)
    mail.setToAddress(MailServer.To)
    mail.setCCAddress(MailServer.CC)
    subject = "pyhton smpt attachment test"
    mail.setSubject(subject)

    #添加普通邮件正文内容
    content = "python smpt email test......"
    mail.addPlainText(content)

    #添加HTML格式邮件正文内容
    msg_html = """
            <p>Python 邮件发送测试...</p>
            <p><a href="http://www.runoob.com">这是runoob链接</a></p>
            """
    mail.addHtmlText(msg_html)

    #将html文件内容显示到邮件正文
    file_name = "./Html/LogTimeWeeklyReport.html"
    msg_html = open(file_name).read()
    mail.addHtmlText(msg_html)

    # 添加附件
    attach_files = ["./Html/DailyReminder.html", "./Html/LogTimeWeeklyReport.html",
                    "./Html/AfternoonReminderHttp.rar", "./Html/DailyReminder.zip",
                    r"./Pictures/gree_tree.png", r"./Pictures/kenan.gif", r"./Pictures/river.jpg",
                    r"./Pictures/skip.jpg", r"./Pictures/tree.png"]
    mail.addAttachFiles(attach_files)

    #添加邮件正文图片
    file_name_list = [r"./Pictures/gree_tree.png", r"./Pictures/kenan.gif", r"./Pictures/river.jpg",
                      r"./Pictures/skip.jpg", r"./Pictures/tree.png"]
    mail.addPictures(file_name_list)

    mail.sendMail()

if __name__ == "__main__":
    sendMail()