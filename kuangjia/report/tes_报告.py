#/usr/bin/env python
# --*-- coding:utf-8 -*-
import unittest
import HTMLTestRunnertest
import time
def run_baogao(ceshi):
    suit = unittest.TestSuite()
    for a in ceshi:
        discover = unittest.defaultTestLoader.discover(r'E:\py\kuangjia\test', pattern='{}.py'.format(a.strip()))
        suit.addTest(discover)
    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    f = open(r'E:\py\kuangjia\report\ab.html', 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(tester='旭方',
                                               description='测试结果如下：',
                                               title='好分数测试报告',
                                               stream=f)
    runner.run(suit)
    f.close()