#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import urllib

class TestUrlHttpCode(unittest.TestCase):
    def setUp(self):
        self.__checkUrls = ['http://www.baidu.com','http://www.163.com',
                            'http://www.sohu.com','http://www.cnpythoner.com']
        print "setUp function invoke!"

    def tearDown(self):
        print "tearDown function invoke!"

    # unittest.TestCase中如果没有以 test 打头的测试用例，则会执行 runTest 测试方法
    def runTest(self):
        for url in self.__checkUrls:
            httpCode = urllib.urlopen(url).getcode()
            self.assertEqual(httpCode, 200)

if __name__ == "__main__":
    unittest.main()