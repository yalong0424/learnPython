#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import math.add as add

class AddTestCase(unittest.TestCase):
    def testAddA(self):
        expected_value = 5
        result = add(2, 3)
        self.assertEqual(result, expected_value, "test case testAddA failed!")

    def testAddB(self):
        expected_value = 5
        result = add(2, 4)
        self.assertEqual(result, expected_value, "test case testAddB failed!")

    def testAddC(self):
        exptected_value = 7
        result = add(3, 3)
        self.assertEqual(exptected_value, result, "test case testAddC failed!")