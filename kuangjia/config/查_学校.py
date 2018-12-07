#/usr/bin/env python
# --*-- coding:utf-8 -*-
import requests
class School_查询():
    def school_快查(self,a):
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
    # def school_考试快查(self,a):
    #     pass
    # def school_学校列表(self):
    #     pass
class Z_Name():
    def name(self,a):
        url='http://127.0.0.1:5000/login'
        payload={'name':'{}'.format(a)}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'text/css,*/*;q=0.1',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        response=requests.get(url=url,headers=headers,data=payload)
        html=response.json()
        return html
