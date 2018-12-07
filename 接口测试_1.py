#/usr/bin/env python
# --*-- coding:utf-8 -*-
#
# """接口测试：发送请求，验证响应是否符合需求的过程
#     requests  发送http请求       assert 断言处理
# unittest:做单元测试的自动化框架————>unittesunittestt.TestCase:测试用例(用例管理)
#                                           .TestSuite:测试套件(测试集)将多个测试用例集合在一个测试套件里
#                                           unittest.TestLoader:测试载入：将测试用例加载到测试套件中
#                                           unittest.TestRunner:执行测试用例
# unittest:封装了检验返回的结果—俗称:断言 """

import requests
import unittest
import HTMLTestRunne
import HTMLTestRunnertest
import time

def tes_schools(a):
    url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
    querystring = {"filterInput": "{}".format(a)}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'text/css,*/*;q=0.1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    # print(response.json()['msg'])
    html = response.json()
    return html
class School(unittest.TestCase):
    # def setUp(self):        #初始化测试环境，保证每一个用例都在相同的环境下执行(在每次测试用例前执行)
    #     print(123)
    def test_1(self):      #测试用例（必须以test开头）
        html=tes_schools('北京')
        try:
            self.assertEqual(html['code'],5)
        except:
            self.assertEqual(html['data'][0]['schoolName'],'大概')

    def test_2(self):
        html=tes_schools('sd')
        self.assertNotEqual(html['code'],0)
    # def tearDown(self):     #清理环境  每一次用例执行之后去执行
        # print('喜爱')
    def test_3(self):
        html=tes_schools('东京')
        self.assertIn(0,html['code'])
    # def test_4(self):
    #     html=tes_schools('@#')
    #     self.
if __name__=='__main__':
    unittest.main()
    #生成测试报告         创建一个测试套件
    suit=unittest.TestSuite()
    #添加测试用例
    # 1，将测试用例添加到测试套件中suit.addTest(类名（测试用例）)
    # suit.addTest(School('test_1'))
    # suit.addTest(School('test_2'))
    # suit.addTest(School('test_3'))
    #2，将整个类中的所有测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(School))
    #设置时间
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open('ab.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(tester='旭方',
                                             description='测试结果如下：',
                                             title='好分数测试报告',
                                             stream=f)
    runner.run(suit)
    f.close()
"""框架：
        config--设置-->配置代码，公共代码
        data--数据---->数据文件，读取数据的代码
        report-测试报告->测试报告，生成测试报告的代码
        log---日志(动作)->日志信息。动作（logging）
        test--测试-->测试代码测试，（文件）模块
        driver--执行-->执行测试用例
        """

