#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mathpackage_demo1.add

class AddTestCase(unittest.TestCase):
    def testAddA(self):
        expected_value = 5
        result = mathpackage_demo1.add.add(2, 3)
        self.assertEqual(result, expected_value, "test case testAddA failed!")

    def testAddB(self):
        expected_value = 5
        result = mathpackage_demo1.add.add(2, 4)
        self.assertEqual(result, expected_value, "test case testAddB failed!")

    def testAddC(self):
        exptected_value = 7
        result = mathpackage_demo1.add.add(3, 3)
        self.assertEqual(exptected_value, result)