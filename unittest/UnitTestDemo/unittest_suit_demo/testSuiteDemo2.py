#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class LuaTest(unittest.TestCase):
    def runTest(self):
        print 'anything'

    def setUp(self):
        # 预置环境
        print '--------------LuaTestsetUp--------------\n'

    def tearDown(self):
        # 清理环境
        print '--------------LuaTestclear--------------\n'

    def test_lua(self):
        print 'test_lua'

    def test_lualog(self):
        print 'test_lualog'


#如果从逻辑意义或者方便的角度出发，将多个TestCase写在了一个.py file中，则可以使用测试套件(测试用例集合) TestSuite 将测试用例组织在一起，
#这样就方便在 测试总入口 处 统一调用所有的测试用例
def casesuite(file=None):
    suite = unittest.TestSuite()
    suite.addTest(LuaTest("test_lua"))
    suite.addTest(LuaTest("test_lualog"))
    if file is None:
        unittest.TextTestRunner().run(suite)
    else:
        unittest.TextTestRunner(stream = file, verbosity=2).run(suite)

if __name__ == "__main__":
    #方式一： 直接调用casesuite() 方法
    #casesuite()

    #方式二：通过 unittest.main()方法调用，只需将defaultTest设置一下即可
    unittest.main(defaultTest="casesuite")