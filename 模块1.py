#/usr/bin/env python
#--*-- coding:utf-8 -*-
import pymysql
# import os
import xlwt
import xlrd
from xlutils.copy import copy
import paramiko
# abc=pymysql.connect(host='192.168.0.22',port=3306,
#                 user='root',password='qwert',
#                 charset='utf8')
# ad=pymysql.connect(host='192.168.0.22',
#                    port=3306,user='root',
#                    password='qwert',
#                    charset='utf8')
# ccc=abc.cursor()
# ccc.execute('use stu;')
# ccc.execute('create table biao1(学号 int,姓名 char(10),年龄 int,班级 char(10));')
# ccc.fetchall()
# b=[]
# for i in range(5):
#     ccc.execute('insert into biao1 values({},"{}",{},"{}");'.format(2000+i,'小张'+'{}'.format(i),23+i,'{}'.format(i)+'班'))
#     a=ad.commit()
#     b.append(a)
# ccc.execute('select * from biao1;')
# for j in ccc.fetchall():
#     print(j)
# ccc.execute('select * from biao1;')
# shuj=ccc.fetchall()
# print(shuj)
# for i in  range(len(shuj)):
#     print(shuj[i])
# ccc.execute('desc biao1;')
# biaot=ccc.fetchall()
# with open('aa.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaot)):
#         if i==len(biaot)-1:
#             print(i)
#             f.write(biaot[i][0]+'\n')
#         else:
#             f.write(biaot[i][0]+' ')
# for i in range(10):
#     with open('aa.txt','a+',encoding='utf8') as g:
#
#             for j in shuj:
#                  g.write('{},{},{},{}'.format(j[0],j[1],j[2],j[3])+'\n')
                # for k in range(len(shuj))：


# f=xlwt.Workbook()
# af =f.add_sheet('python操作stu1')
# af.write(0,0,'学号')
# af.write(0,1,'姓名')
# af.write(0,2,'年龄')
# af.write(0,3,'班级')
# af.write(0,4,'成绩')
# d=[2000,'小张',22,'班',70]
# for i in range(10):
#     for j in range(5):
#         af.write(i+1,j,d[j])
# f.save('text.xls')


# f=xlwt.Workbook()
# a=f.add_sheet('python操作学生表')
# a.write(0,0,'姓名')
# a.write(0,1,'年龄')
# a.write(0,2,'班级')
# for i in range(10):
#     a.write(i+1, 0, '小张')
#     a.write(i+1, 1, '23')
#     a.write(i+1, 2, '一般')
# f.save('text.xls')


# f=xlwt.Workbook()
# ab=f.add_sheet('python操作Excel')
# ab.write(0,0,'学号')
# ab.write(0,1,'姓名')
# ab.write(0,2,'班级')
# ab.write(0,3,'性别')
# ab.write(0,4,'成绩')
# ab.write(0,5,'家庭电话')
# for i in range(5):
#     ab.write(i+1,0,2000+i)
#     ab.write(i+1,1,'{}'.format(i)+'小张')
#     ab.write(i+1,2,('{}'.format(i))+'班')
#     ab.write(i+1,3,'男')
#     ab.write(i+1,4,69+i)
#     ab.write(i+1,5,1583762+i+i+i+34)
#     f.save('rrr.xls')

# f=xlrd.open_workbook('text.xls')
# sheet=f.nsheets
# print(sheet)
# sheet=f.sheets()[0]
# print(sheet.row_values(0))
# print(sheet.nrows)
# # print(sheet.ncols)
# # print(sheet.col_values(1))
# # print(sheet.cell(0,1).value)
import pymysql
import xlrd
# abc=pymysql.connect(host='192.168.0.22',              #xls导入库
#                     port=3306,
#                     user='root',
#                     password='qwert',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('use stu;')
# f=xlrd.open_workbook('text.xls')
# sheet=f.sheets()[0]
# b=sheet.nrows
# a=sheet.row_values(0)
# print(b)
# aaa.execute('create table xla({} char(10),{} char(10),{} char(10));'.format(a[0],a[1],a[2]))
# for i in range(1,b):
#     print(i)
#     shuju=sheet.row_values(i)
#     aaa.execute('insert into xla values("{}","{}","{}");'.format(shuju[0],shuju[1],shuju[2]))


# import xlrd                                                     #xls表导入文件txt
# import  xlwt
# f=xlrd.open_workbook('rrr.xls')
# sheet=f.sheets()[0]
# s=sheet.nrows
# ##c=[]
# for i in range(s):
#     # print(i)
#     shuju=sheet.row_values(i)
#     print(shuju)
    ## c.append(shuju)
    # if i==0:
    #     with open('txtsd.txt','w',encoding='utf-8') as f:
    #         f.write('{},{},{},{},{},{}'.format(shuju[0],shuju[1],shuju[2],shuju[3],shuju[4],shuju[-2],shuju[-1])+'\n')
    # else:
    #     with open('txtsd.txt','a',encoding='utf-8') as g:
    #         g.write('{},{},{},{},{},{}'.format(shuju[0],shuju[1],shuju[2],shuju[3],shuju[4],shuju[-2],shuju[-1])+'\n')


# import xlwt                             #txt导入xls
# import xlrd
# c=[]
# with open('txts.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
#     for k in a:
#         b=k.replace('\n','').split(',')
#         c.append(b)
# print(c)
#         # print(b)
# g = xlwt.Workbook()
# sheet=g.add_sheet('txt转入xls')
# for i in range(len(a)):
#     for j in range(len(b)):
#         print(c[i][j])
#         sheet.write(i,j,c[i][j])
# g.save('vv.xls')

# import pymysql
# abc=pymysql.connect(host='192.168.0.22',           #TXT导入函数库
#                     port=3306,
#                     user='root',
#                     password='qwert',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('use stu;')
# c=[]
# with open('txts.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
#     print(a)
    # for i in a:
    #     b=i.replace('\n', '').split(',')
        # print(b[-1])
    #     c.append(b)
    # print(c)
    # # aaa.execute('create table ss ({} char(10),{} char(10),{} char(10),{} char(10));'.format(c[0][0],c[0][1],c[0][2],c[0][-1]))
    # for j in range(len(c)):
    #     print(j)
    #     if j==len(c)-1:
    #         break
    #     aaa.execute('insert into ss values("{}","{}","{}","{}");'.format(c[j+1][0],c[j+1][1],c[j+1][2],c[j+1][-1]))
    #     abc.commit()






# os.chdir(r'E:\QQ\1241378256\FileRecv')             #删除以.py结尾的文件
# e=os.listdir(r'E:\QQ\1241378256\FileRecv')
# print(e)
# a=0
# b=0
# for i in e:
#     if os.path.isfile(i):
#         a+=1
#     elif os.path.isdir(i):
#         b+=1
# print(a,b)
# import os
# a=os.popen('nslookup www.baidu.com')
# print(a.read())
# print(os.getcwd())
# os.chdir(r'E:\py')
# os.mkdir('abc')
# os.makedirs(r'abc\ab\ac')
# os.removedirs(r'abc\ab\ac')
# os.mkdir('aaa')
# os.rmdir('aaa')
# print(os.listdir(r'D:\Python\Python36'))
# os.rename('hanshu.py','模块.py')
# print(os.path.split(r'E:\py\day1day.py\fff.py'))
# print(os.path.splitext(r'E:\py\day1day.py\fff.py'))
# print(os.path.isfile('day1.py'))
# print(os.path.isdir('dsf.py'))
# print(os.path.islink('fsd.py'))
# print(os.listdir())
# for i in os.listdir():
#     if os.path.splitext(i)[-1]=='.py':
#         print(i)
# print()
import os
for i  in os.listdir():
    if os.path.isfile(i):
        print(i)
# print()
# for i in os.listdir():
#     if os.path.isdir(i):
#         print(i)


# import pymysql                                          #哭到表
# import xlwt
# abc=pymysql.connect(host='192.168.0.22',
#                     user='root',
#                     port=3306,
#                     password='qwert',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('use stu;')
# aaa.execute('desc ss;')
# biaot=aaa.fetchall()
# # print(biaot[0][0])
# aaa.execute('select * from ss;')
# shuj=aaa.fetchall()
# print(shuj[0])
# f=xlwt.Workbook()
# ab=f.add_sheet('mysql导入xls')
# for i in range(len(biaot)):
#     ab.write(0,i,biaot[i][0])
#     for j in range(len(shuj)):
#         # for k in range(len(biaot)):
#             ab.write(j+1,i,shuj[j][i])
# f.save('nx.xls')


