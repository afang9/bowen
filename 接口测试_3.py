#--*-- coding:utf-8 -*-
import unittest
import requests
import HTMLTestRunnertest
import xlrd
import time
class School(unittest.TestCase):
    def read_shuju(self):
        shuju=[]
        f=xlrd.open_workbook(r'e:\py\北京\北京.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(1,num):
            aa=sheet.row_values(i)
            shuju.append(aa)
        return shuju
    def tes_school(self,a):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring={'filterInput':'{}'.format(a)}
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'text/css,*/*;q=0.1',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        response=requests.get(url=url,headers=headers,params=querystring)
        html=response.json()
        return html
    def test_1(self):
        shuju=self.read_shuju()
        html=self.tes_school(shuju[0][0])
        try:
            self.assertEqual(html['code'],int(shuju[0][1]))
        finally:
            self.assertIn(len(html['data']),range(int(shuju[0][2])))
    def test_2(self):
        shuju=self.read_shuju()
        html=self.tes_school(shuju[1][0])
        try:
            self.assertNotEqual(len(html['data']),range(int(shuju[1][2])))
        finally:
            self.assertEqual(html['code'],int(shuju[1][1]))
    def test_3(self):
        shuju=self.read_shuju()
        html=self.tes_school(shuju[2][0])
        try:
            self.assertIsNone(html['code'],int(shuju[2][1]))
        finally:
            self.assertIsNotNone(len(html['data']),int(shuju[2][1]))
if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(School))
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open('wuw.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(tester='李旭方',
                                             description='测试结果如下——',
                                             title='好分数报告',
                                             stream=f)
    runner.run(suit)
    f.close()
