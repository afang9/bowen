#/usr/bin/env python
#--*-- coding:utf-8 -*-
import requests
import unittest
"""接口测试：发送请求，验证响应是否符合需求的过程
    requests  发送http请求       assert 断言处理
unittest:做单元测试的自动化框架————>unittest.TestCase:测试用例(用例管理)
                                          unittest.TestSuite:测试套件(测试集)将多个测试用例集合在一个测试套件里
                                          unittest.TestLoader:测试载入：将测试用例加载到测试套件中
                                          unittest.TestRunner:执行测试用例
unittest:封装了检验返回的结果—俗称:断言 """

# a='北京'
# a=input('请输入学校::')
# class School():
#     def test_schools(self,a):
#         url='http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring={"filterInput":"{}".format(a)}
#         headers={
#                 'Content-Type':'application/x-www-form-urlencoded',
#                 'accept':'text/css,*/*;q=0.1',
#                 'accept-encoding':'gzip, deflate, br',
#                 'accept-language':'zh-CN,zh;q=0.9',
#                 'Cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
#                 }
#         response=requests.get(url=url,headers=headers,params=querystring)
#         # print(response.json()['msg'])
#         html=response.json()
#         return html
#
#
#         assert html['code']==0

