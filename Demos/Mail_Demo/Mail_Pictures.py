#!/usr/bin/python
# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from Mail_Multi_Base import Mail_Base
from utils import MailServer

class Mail_Picture(Mail_Base):
    def __init__(self):
        super(Mail_Picture, self).__init__()
        self.msg_alternative = MIMEMultipart("alternative")
        self.msg_root.attach(self.msg_alternative)
        self.__addHtmlContent()

    def __addHtmlContent(self):
        html_msg = """
        <p>Python Pictures 邮件测试</p>
        <p><a href="http://www.runoob.com">菜鸟教程</a></p>
        <p>图片演示：</p>
        <p><img src="cid:image_tree"></p>
        """
        content = MIMEText(html_msg, "html", "utf-8")
        self.msg_alternative.attach(content)

    def addPicture(self, file_picture):
        fp = open(file_picture, "rb")
        msg_image = MIMEImage(fp.read())
        fp.close()
        #定义图片ID，在HTML中引用
        msg_image.add_header("Content-ID", "<image_tree>")
        self.msg_root.attach(msg_image)


class Mail_Multi_Picture(Mail_Base):
    def __init__(self):
        super(Mail_Multi_Picture, self).__init__()
        self.msg_alternative = MIMEMultipart("alternative")
        self.msg_root.attach(self.msg_alternative)

    def addPictures(self, picture_file_list):
        html_msg = """
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
            html_msg += "<p><img src='cid:%s'></p>"%picture_id

            #定义图片ID，在HTML中引用
            msg_image.add_header("Content-ID", "<%s>"%picture_id)
            self.msg_root.attach(msg_image)

        #添加邮件正文（包含图片的HTML内容）
        content = MIMEText(html_msg, "html", "utf-8")
        self.msg_alternative.attach(content)

def sendMail_Picture():
    mail = Mail_Picture()
    mail.setFromAddress(MailServer.FROM)
    mail.setToAddress(MailServer.To)
    mail.setCCAddress(MailServer.CC)
    subject = "pyhton smpt attachment test"
    mail.setSubject(subject)

    file_name = r"./Pictures/gree_tree.png"
    mail.addPicture(file_name)

    mail.sendMail()

def sendMail_Pictures():
    mail = Mail_Multi_Picture()
    mail.setFromAddress(MailServer.FROM)
    mail.setToAddress(MailServer.To)
    mail.setCCAddress(MailServer.CC)
    subject = "pyhton smpt attachment test"
    mail.setSubject(subject)

    file_name_list = [r"./Pictures/gree_tree.png", r"./Pictures/kenan.gif", r"./Pictures/river.jpg",
                      r"./Pictures/skip.jpg", r"./Pictures/tree.png"]
    mail.addPictures(file_name_list)

    mail.sendMail()

if __name__ == "__main__":
    sendMail_Picture()