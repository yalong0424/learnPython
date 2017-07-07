#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mathpackage_demo1.divide import devide

class DevideTestCase(unittest.TestCase):
    def testDevideA(self):
        expected_value = 2
        result = devide(8, 4)
        self.assertEqual(expected_value, result, "test case testDevideA failed!")

    def testDevideB(self):
        expected_value = 3
        result = devide(8, 4)
        self.assertEqual(expected_value, result, "test case testDevideB failed!")

    def testDevideC(self):
        expected_value = 5
        result = devide(10, 3)
        self.assertEqual(result, expected_value)