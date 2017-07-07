#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.cnblogs.com/idbeta/archive/2015/12/11/5040187.html

import os
from mathTestSuitDemo1 import suite
from testSuiteDemo2 import casesuite

#如果接口相当多，为了方便维护，建议每个case用独立的py来写，然后用一个“总入口”去import所有py，然后再调用就行了
if __name__ == '__main__':
    # 如果要保存unitest的测试输出日志到指定文件，则需要用到TextTestRunner
    fileName = ".." + os.path.sep + "unittest_log_suit.txt"
    file = open(fileName, "w")
    casesuite(file)
    suite(file)
    file.close()