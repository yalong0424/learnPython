#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cnblogs.com/51kata/p/5887940.html
# http://www.cnblogs.com/idbeta/archive/2015/12/11/5040187.html

import sys
import os
import unittest
from addtestcase import AddTestCase
from minustestcase import MinusTestCase
from multiplytestcase import MultiplyTestCase
from devidetestcase import DevideTestCase

sys.path.append(".")
sys.path.append("..")

if __name__ == '__main__':
    #如果要保存unitest的测试输出日志到指定文件，则需要用到TextTestRunner
    fileName = ".." + os.path.sep + "unittest_log_main.txt"
    file = open(fileName, "w")
    runner = unittest.TextTestRunner(stream = file, verbosity = 2)
    unittest.main(exit = False, testRunner = runner)
    file.close()

    #如果不需要保存unitest的测试输出日志到指定文件，则只需直接调用unittest.main()方法即可
    #unittest.main()