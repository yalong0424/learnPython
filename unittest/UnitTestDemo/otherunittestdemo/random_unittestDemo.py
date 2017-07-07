#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://blog.csdn.net/hackerain/article/details/24095117

import unittest
import random

class TestSequenceFuncs(unittest.TestCase):
    '''
    this class used to test random sequence functions with unittest.
    '''
    def setUp(self):
        '''
        setUp function used to init resources before test case execute!
        :return: None
        '''
        self.__seq = range(10)
        print "setUp function to init resources!!!"

    def tearDown(self):
        '''
        tearDown function used to free resources after test case execute!
        :return: None
        '''
        print "tearDown function to free resources!!!"

    def test_shuffleA(self):
        '''
        this function used to test random.shuffle function!
        :return: test succeed
        '''
        random.shuffle(self.__seq)
        self.__seq.sort()
        self.assertEqual(self.__seq, range(10), "test case test_shuffleA failed!")

        #should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_shuffleB(self):
        '''
        this function used to test random.shuffle function!
        :return: test failed
        '''
        random.shuffle(self.__seq)
        self.__seq.sort()
        self.assertNotEqual(self.__seq, range(10), "test case test_shuffleB failed!")

        #should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choiceA(self):
        '''
        this function used to test random.choice function!
        :return: test succeed
        '''
        elem = random.choice(self.__seq)
        self.assertTrue(elem in self.__seq, "test case test_choiceA failed!")

    def test_choiceB(self):
        '''
        this function used to test random.choice function!
        :return: test failed
        '''
        elem = random.choice(self.__seq)
        self.assertFalse(elem in self.__seq, "test case test_choiceB failed!")

    def test_samepleA(self):
        '''
        this function used to test random.sample function!
        :return: test succeed
        '''
        with self.assertRaises(ValueError):
            random.sample(self.__seq, 20)

        for elem in random.sample(self.__seq, 5):
            self.assertTrue(elem in self.__seq, "test case test_sampleA failed!")

    def test_samepleB(self):
        '''
        this function used to test random.sample function!
        :return: test failed
        '''
        with self.assertRaises(ValueError):
            random.sample(self.__seq, 20)

        for elem in random.sample(self.__seq, 5):
            self.assertTrue(elem in self.__seq, "test case test_sampleB failed!")

if __name__ == "__main__":
    unittest.main()