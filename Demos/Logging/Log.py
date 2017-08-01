#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

def log_screen():
    """
    实例1：简单的将日志打印到屏幕
    默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
    日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
    """
    logging.debug("this is a debug msg")
    logging.info("this is a info msg")
    logging.warning("this is a warning msg")

def log_config_file():
    """
    实例2：通过logging.basicConfig函数对日志的输出格式及方式做相关配置

    logging.basicConfig函数各参数:
    filename: 指定日志文件名
    filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
    format: 指定输出的格式和内容，format可以输出很多有用信息，如下例所示:
     %(levelno)s: 打印日志级别的数值
     %(levelname)s: 打印日志级别名称
     %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
     %(filename)s: 打印当前执行程序名
     %(funcName)s: 打印日志的当前函数
     %(lineno)d: 打印日志的当前行号
     %(asctime)s: 打印日志的时间
     %(thread)d: 打印线程ID
     %(threadName)s: 打印线程名称
     %(process)d: 打印进程ID
     %(message)s: 打印日志信息
    datefmt: 指定时间格式，同time.strftime()
    level: 设置日志级别，默认为logging.WARNING
    stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
    """
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                        datefmt="%a, %d %b %Y %H:%M:%S", filename="myapp.log", filemode="w")

    logging.debug("this is a debug message")
    logging.info("this is a info message")
    logging.warning("this is a warning message")


def log_screen_file():
    """
    实例3：将日志同时输出到日志和屏幕
    """
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                        datefmt="%a, %d %b %Y %H:%M:%S", filename="myapp_2.log", filemode="w")

    ##########################################################################################################
    #定义一个StreamHandler，将INFO级别或者更高级别的日志信息打印到标准错误，并将其添加到当前的日志处理对象
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    ##########################################################################################################

    logging.debug("this is a debug info")
    logging.info("this is a info info")
    logging.warning("this is a warning info")


def log_rotating():
    """
    实例4：logging之日志轮替
    """
    from logging.handlers import RotatingFileHandler
    ##########################################################################################################
    #定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
    RtFileHandler = RotatingFileHandler("myapp_3.log", maxBytes=10*1024*1024,backupCount=5)
    RtFileHandler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    RtFileHandler.setFormatter(formatter)
    logging.getLogger("").addHandler(RtFileHandler)
    ##########################################################################################################


"""
从实例3（log_screen_file）和实例4（log_rotating）可以看出，logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。
logging的几种handle方式如下：

    logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
    logging.FileHandler: 日志输出到文件
    日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
    logging.handlers.BaseRotatingHandler
    logging.handlers.RotatingFileHandler
    logging.handlers.TimedRotatingFileHandler
    logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
    logging.handlers.DatagramHandler:  远程输出日志到UDP sockets
    logging.handlers.SMTPHandler:  远程输出日志到邮件地址
    logging.handlers.SysLogHandler: 日志输出到syslog
    logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
    logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
    logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器

由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中。    
"""

if __name__ == "__main__":
    log_screen()
    log_config_file()
    log_screen_file()
    log_rotating()