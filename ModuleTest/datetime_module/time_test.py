#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

#time.time()函数返回从EPOCH（1970年1月1日 00:00:00）开始到现在的秒数。
print("time.time(): ", time.time())

'''
time.localtime(seconds)和time.gmtime(seconds)都返回时间元祖，即返回tuple格式的时间表示。
两者的区别是：time.gmtime(seconds)返回的是相对于0时区的时间元祖表示，而time.localtime(seconds)返回的是相对于当前时区的时间值。
时间元祖表示为：
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=16, tm_hour=17, tm_min=38, tm_sec=58, tm_wday=2, tm_yday=228, tm_isdst=0)
'''
print("time.localtime(seconds): ",time.localtime())
print("time.gmtime(seconds): ", time.gmtime())