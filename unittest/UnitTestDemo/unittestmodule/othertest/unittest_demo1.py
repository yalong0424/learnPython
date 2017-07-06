#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#将被测方法、测试类以及测试总入口放在一个模块中示例

#被测方法
def cal(x, y):
    return x + y

#测试类
class CalTest(unittest.TestCase):
    def testA(self):
        expected_value = 6
        result = cal(2, 4)
        self.assertEqual(expected_value, result, "test case testA failed")

    def testB(self):
        expected_value = 3
        result = cal(2, 2)
        self.assertEqual(expected_value, result, "test case testB failed")

    def testC(self):
        expected_value = 6
        result = cal(2, 5)
        self.assertEqual(expected_value, result)

    #测试方法必须以 test 打头，否则就不会被执行
    def notteststart(self):
        expected_value = 8
        result = cal(2, 6)
        self.assertEqual(expected_value, result, "test case notteststart failed")

#执行所有测试代码
if __name__  == '__main__':
    unittest.main()