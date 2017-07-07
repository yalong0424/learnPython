#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cnblogs.com/idbeta/archive/2015/12/11/5040187.html

import unittest
import sys
import platform
import mathpackage_demo1.add
from mathpackage_demo1.minus import minus

class AddTestCase(unittest.TestCase):
    # 如果不是TestCase中的每个test开头的测试用例都需要预置和清理环境，而是
    # 每个class用一次，即每个test开头的测试用例要么不需要预置和清理环境，要么预置和清理环境的方法完全一样，
    # 则只需要用setUpClass、tearDownClass代替setUp、tearDown即可，
    # 如果是整个文件只需要用一次，则要用 setUpModule() 和 tearDownModule() 这两个函数了，注意是函数，与 TestCase 类同级

    #setUpClass/tearDownClass 方法在TestCase中所有test开头的测试用例执行开始前和所有用例执行完毕后调用，一个TestCase类执行过程中只调用一次
    @classmethod
    def setUpClass(cls):
        print "AddTestCase 预置环境：测试用例执行前测试环境的搭建"

    @classmethod
    def tearDownClass(cls):
        print "AddTestCase 清理环境：测试用例执行后测试环境的销毁"

    def testAddA(self):
        expected_value = 5
        result = mathpackage_demo1.add.add(2, 3)
        self.assertEqual(result, expected_value, "test case testAddA failed!")

    def testAddB(self):
        expected_value = 5
        result = mathpackage_demo1.add.add(2, 4)
        self.assertEqual(result, expected_value, "test case testAddB failed!")

    #无条件跳过 testAddC 这个测试用例
    @unittest.skip("I do not want to execute this test case!")
    def testAddC(self):
        exptected_value = 7
        result = mathpackage_demo1.add.add(3, 3)
        self.assertEqual(exptected_value, result)

    def testAddD(self):
        expected_value = 6
        result = mathpackage_demo1.add.add(2, 4)
        self.assertEqual(result, expected_value, "test case testAddD failed!")

class NginxTestCase(unittest.TestCase):
    #使用setUp、tearDown预置和清理测试环境时，该TestCase下的每一个以test开头的测试用例在执行前和执行后都需要调用一次这两个方法，
    #即TestCase中的每一个以test打头的测试用例都需要分别进行测试前和测试后的预置和清理环境。
    def setUp(self):
        print "----------------------NginxTestCase setUp---------------------------"

    def tearDown(self):
        print "----------------------NginxTestCase tearDown-------------------------"

    def test_nginx(self):
        print "test_nginx test case"

    def test_nginxLog(self):
        print "test_nginxLog test case"

    #无条件跳过 test_mustSkip 这个用例
    @unittest.skip("must skip this test case!!!")
    def test_mustSkip(self):
        print "test_mustSkip test case"

    #根据条件判断是否执行 test_mayBeSkip 这个用例，当添加为 False 时，跳过
    @unittest.skipUnless(sys.platform.lower().startswith("linux"), "requires windows")
    def test_mayBeSkip(self):
        print "test_mayBeSkip test case"

    #根据条件判断是否执行 test_mayBeSkip2 这个用例，当条件为 True 时跳过
    @unittest.skipIf(platform.system().lower().startswith("linux"), "require windows")
    def test_mayBeSkip2(self):
        print "test_mayBeSkip2 test case"

    #手动将TestCase中非 test 开头的测试用例添加到 TestSuite 中时，该非以 test 开头的测试用例也会被执行
    #强烈建议，TestCase中的测试用例必须以 test 开头
    def suit_1(self):
        print "suit_1"

    # 手动将TestCase中非 test 开头的测试用例添加到 TestSuite 中时，该非以 test 开头的测试用例也会被执行
    # 强烈建议，TestCase中的测试用例必须以 test 开头
    def myTest(self):
        print "myTest function"

class MinusTestCase(unittest.TestCase):
    #当TestCase中的所有测试用例都不需要执行测试前和测试后的预置和清理环境工作时，就不需要实现setUp和tearDown。
    #同样的，因为每个接口的预置环境可能不一样，所以每个接口的用例应该都用单独class来包含，不过每个class的用例都还是要用test开头
    def testMinusA(self):
        expected_value = 3
        result = minus(5, 2)
        self.assertEqual(expected_value, result, "test case testMinusA failed!")

    def testMinusB(self):
        expected_value = 4
        result = minus(6, 3)
        self.assertEqual(expected_value, result, "test case testMinusB failed!")

    def testMinusC(self):
        expected_value = 2
        result = minus(5, 2)
        self.assertEqual(result, expected_value)

#如果从逻辑意义或者方便的角度出发，将多个TestCase写在了一个.py file中，则可以使用测试套件(测试用例集合) TestSuite 将测试用例组织在一起，
#这样就方便在 测试总入口 处 统一调用所有的测试用例
def suite(file=None):
    suit = unittest.TestSuite()
    suit.addTest(AddTestCase("testAddA"))
    suit.addTest(AddTestCase("testAddC"))
    suit.addTest(AddTestCase("testAddD"))
    suit.addTest(NginxTestCase("test_nginx"))
    testCaseList = [NginxTestCase("test_mustSkip"), NginxTestCase("test_mayBeSkip"),
                    NginxTestCase("test_mayBeSkip2"), NginxTestCase("suit_1")]
    suit.addTests(testCaseList)
    suit.addTest(NginxTestCase("myTest"))
    suit.addTest(MinusTestCase("testMinusB"))
    suit.addTest(MinusTestCase("testMinusC"))
    #没有添加到TestSuite中的用例： AddTestCase.testAddB 和 NginxTestCase.test_nginxLog 以及 MinusTestCase.testMinusA 不会被执行
    if file is None:
        unittest.TextTestRunner().run(suit)
    else:
        unittest.TextTestRunner(file).run(suit)

if __name__ == "__main__":
    # unittest.main(exit = False,verbosity=2)#它是全局方法，把它屏蔽后，不在suite的用例就不会跑，
    # exit = False表示中间有用例失败也继续执行；还有比较常用的verbosity=2，表示显示def名字

    #方式一：直接调用 suite() 方法
    #suite()

    #方式二： 通过 unittest.main()方法调用，只需将defaultTest设置一下即可
    unittest.main(defaultTest="suite")