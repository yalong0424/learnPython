#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mathpackage_demo1.minus

class MinusTestCase(unittest.TestCase):
    def testMinusA(self):
        expected_value = 3
        result = mathpackage_demo1.minus.minus(5, 2)
        self.assertEqual(expected_value, result, "test case testMinusA failed!")

    def testMinusB(self):
        expected_value = 4
        result = mathpackage_demo1.minus.minus(6, 3)
        self.assertEqual(expected_value, result, "test case testMinusB failed!")

    def testMinusC(self):
        expected_value = 2
        result = mathpackage_demo1.minus.minus(5, 2)
        self.assertEqual(result, expected_value)