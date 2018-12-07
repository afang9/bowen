#usr/bin/env python
#--*-- coding:utf-8 -*-
import requests
class School():
    def shool_search(self,a):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring={'filterInput':'{}'.format(a)}
        head={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        response=requests.get(url=url,headers=head,params=querystring)
        html=response.json()
        return html