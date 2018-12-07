#/usr/bin/env python
# --*-- coding:utf-8 -*-
import requests
import unittest
import HTMLTestRunne
import HTMLTestRunnertest
import time
import xlrd
class School(unittest.TestCase):
    def tes_shuju(self):
        shuju=[]
        f=xlrd.open_workbook('北京.xlsx')
        # sheet=f.nsheets
        sheet=f.sheets()[0]
        num=sheet.nrows
        # print(num)
        for i in range(1,num):
            aa=sheet.row_values(i)
            shuju.append(aa)
        print(shuju[0][0])
        return shuju
# s=School()
# s.tes_shuju()

    def tes_schools(self,a):
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
        html = response.json()
        return html
# class School(unittest.TestCase):

    def test_1(self):
        shuju=self.tes_shuju()
        html=self.tes_schools(shuju[0][0])
        try:
            self.assertEqual(html['code'],int(shuju[0][1]))
        except:
            self.assertEqual(len(html['data']),range(int(shuju[1][2])))

    def test_2(self):
        shuju=self.tes_shuju()
        html=self.tes_schools(shuju[1][0])
        self.assertNotEqual(html['code'],int(shuju[1][1]))
        self.assertEqual(len(html['data']),range(int(shuju[2][2])))
    def test_3(self):
        shuju=self.tes_shuju()
        html=self.tes_schools(shuju[0][0])
        self.assertEqual(html['code'],int(shuju[2][1]))
# s=School()
# s.tes_shuju()
if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(School))
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open('ab.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(tester='旭方',
                                             description='测试结果如下：',
                                             title='好分数测试报告',
                                             stream=f)
    runner.run(suit)
    f.close()