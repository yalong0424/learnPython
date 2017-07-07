#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################
# http://blog.csdn.net/five3/article/details/7104466
##############################################

import unittest
import re
import os
import sys

#该函数是一个完整的单元测试的组织代码，会自动遍历执行指定目录下某规范命名的所有文件内的规范书写的测试用例。

#首先要求将所有测试文件规范在放置在指定目录下进行组织，并且要求所有的测试文件均以 testcase.py 结尾，
# 而该函数的作用就是遍历当前目录下所有文件，过滤出所有以 testcase.py 结尾的文件，然后依次执行
# 所有以 testcase.py 结尾的文件中的所有规范书写的TestCase。

#因此，之后，如果新增测试用例，则只需新增一个测试用例的 .py文件，并将该文件按照规范命名后放置在指定目录下，
#除此之外，无需再进行任何修改，该新增文件内的测试用例就会被自动加载执行。
def executeAllTestCases():
    """
    this function will traverse all the files to filter files ended with testcase.py, and then execute the the test cases
        in the filtered files automatically.
    :return:
    """
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    files = os.listdir(path)
    testReg = re.compile(r".*testcase.py", re.IGNORECASE)
    files = filter(testReg.search, files)
    fileNameToModuleName = lambda file: os.path.splitext(file)[0]
    moduleNames = map(fileNameToModuleName, files)
    modules = map(__import__, moduleNames)

    loader = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(loader, modules))

if __name__ == "__main__":
    #运行 unittest.main() 方法时指定 defaultTest 参数值，该参数值为一个 function， 该function会返回一个 unittest.TestSuite实例
    unittest.main(defaultTest="executeAllTestCases")