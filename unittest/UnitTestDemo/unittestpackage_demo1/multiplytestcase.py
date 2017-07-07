#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mathpackage_demo1.multiply import multiply

class MultiplyTestCase(unittest.TestCase):
    def testMultiplyA(self):
        expected_value = 6
        result = multiply(2, 3)
        self.assertEqual(expected_value, result, "test case testMultiplyA failed!")

    def testMultiplyB(self):
        expected_value = 5
        result = multiply(2, 3)
        self.assertEqual(result, expected_value, "test case testMultiplyB failed!")

    def testMultiplyC(self):
        expected_value = 7
        result = multiply(2, 4)
        self.assertEqual(result, expected_value)