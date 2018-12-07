#/usr/bin/env python
# --*-- coding:utf-8 -*-
import unittest
import time
import HTMLTestRunnertest
from kuangjia.test.test_学校 import School
from kuangjia.test.test_学生 import G1
from kuangjia.test.test_另类 import G2
class Tes_run():
    def run_manny(self):
        suit=unittest.TestSuite()
        suit.addTest(unittest.makeSuite(School))
        suit.addTest(unittest.makeSuite(G1))
        suit.addTest(unittest.makeSuite(G2))
        now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f=open('ab.html','wb')
        runner=HTMLTestRunnertest.HTMLTestRunner(tester='旭方',
                                                 description='测试结果如下：',
                                                 title='好分数测试报告',
                                                 stream=f)
        runner.run(suit)
    def run_all(self):
        suit = unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(r'E:\py\kuangjia\test',pattern='test*.py')
        suit.addTest(discover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open('ab.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='旭方',
                                                   description='测试结果如下：',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()
run=Tes_run()
with open('实例.txt','r') as g:
    ceshi=g.read().split('\n')
    print(ceshi)
# for i in ceshi:
#     ff=open(r'E:\py\kuangjia\test\{}.py'.format(i),'r')
#     aa=ff.read()
#     print(aa)

    # for j in c:
    #     jjj=j.split('(')

    # m=globals()["{}".format(jjj[0])]
if __name__=='__main__':


    # if 'all' in ceshi:
     run.run_all()
    # else:
    #     run.run_manny()
