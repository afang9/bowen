#/usr/bin/env python
# --*-- coding:utf-8 -*-
import unittest
import HTMLTestRunnertest
import time
def run_report(c):
    suit=unittest.TestSuite()
    for i in c:
        discover=unittest.defaultTestLoader.discover(r'E:\py\web框架\Tes_test',pattern='{}'.format(i.strip()))
        suit.addTest(discover)
        now=time.strftime('%Y %M %d %H-%M-%S',time.localtime(time.time()))
        f=open(r'E:\py\web框架\report\ab.html', 'wb')
        runner=HTMLTestRunnertest.HTMLTestRunner(tester='李旭方',
                                                 description='测试结果如下',
                                                 title='未登录',
                                                 stream=f)
        runner.run(suit)
        f.close()
