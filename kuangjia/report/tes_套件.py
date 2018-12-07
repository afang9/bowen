import HTMLTestRunnertest
import unittest
import time
# from kuangjia.config.s_school import School
class External_Member():
    def generate_report(self,ceshi):
        suit=unittest.TestSuite()
        for i in ceshi:
            discover=unittest.defaultTestLoader.discover(r'E:\py\kuangjia\test','{}.py'.format(i))
            suit.addTest(discover)
        now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f=open(r'E:\py\kuangjia\report\baogao.html','wb')
        runner=HTMLTestRunnertest.HTMLTestRunner(tester='李旭方',
                                                 description='好分数测试结果',
                                                 title='好分数测试用例问题细节',
                                                 stream=f)
        runner.run(suit)
        f.close()
