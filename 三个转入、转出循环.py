#/usr/bin/env python
#--*-- coding:utf-8 -*-



# import pymysql
# ab=pymysql.connect(host='192.168.0.22',user='root',password='qwert',charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# aa.execute('desc biao1;')
# a=aa.fetchall()
# aa.execute('select * from biao1;')
# b=aa.fetchall()
# print(b)
# with open('MySQL导入TXT.txt','w',encoding='utf-8')as f:
#     for i in range(len(a)):
#         f.write('{}'.format(a[i][0])+',')
#     f.write('\n')
#     for j in range(len(b)):
#         for k in range(len(b[0])):
#             f.write('{}'.format(b[j][k])+',')
#         f.write('\n')
# import pymysql
# ab=pymysql.connect(host='192.168.0.22',user='root',password='qwert',port=3306,charset='utf8')
# aa=ab.cursor()
# c=[]
# with open('MySQL导入TXT.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     print(a)
# aa.execute('use stu;')
# for i in a:
#     b=i.replace(',\n','').split(',')
#     c.append(b)
# for k in range(len(c)):
#     # for j in range(len(c[0])):
#         if k==0:
#             # pass
#             aa.execute('create table biao6 ({} char(10),{} char(10),{} char(10),{} char(10));'.format(c[k][0],c[k][1],c[k][-2],c[k][-1]))
#         else:
#             aa.execute('insert into biao6 values("{}","{}","{}","{}");'.format(c[k][0],c[k][1],c[k][-2],c[k][-1]))
import xlwt
with open('txts.txt','r',encoding='utf-8')as f:
    a=f.readlines()
f=xlwt.Workbook()
sheet=f.add_sheet('TXT导入xls')
c=[]
for i in a:
    b=i.replace('\n','').split(',')
    c.append(b)
for j in range(len(c)):
    for k in range(len(c[0])):
        sheet.write(j,k,c[j][k])
f.save('txt导入xls.xls')
# import xlrd
# f=xlrd.open_workbook('txt导入xls.xls')
# sheet=f.nsheets
# sheet=f.sheets()[0]
# with open('xls导入TXT.txt','w',encoding='utf-8')as f:
#     for i in range(sheet.nrows):
#         for j in range(sheet.ncols):
#             a=sheet.row_values(i)
#             print(a)
#
#             f.write('{}'.format(a[j])+',')
#         f.write('\n')
# import pymysql
# import xlwt
# ab=pymysql.connect(host='192.168.0.22',user='root',password='qwert',port=3306,charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# aa.execute('desc biao1;')
# a=aa.fetchall()
# aa.execute('select * from biao1;')
# b=aa.fetchall()
# f=xlwt.Workbook()
# sheet=f.add_sheet('MySQL导入xls')
# for j in range(len(b[0])):
#         sheet.write(0,j,a[j][0])
# for i in range(len(b)):
#     for k in range(len(b[0])):
#         sheet.write(i+1,k,b[i][k])
# f.save('MySQL导入xls.xls')
# import pymysql
# import xlrd
# ab=pymysql.connect(host='192.168.0.22',user='root',password='qwert',port=3306,charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# f=xlrd.open_workbook('MySQL导入xls.xls')
# sheet=f.nsheets
# sheet=f.sheets()[0]
# c=[]
# for i in range(sheet.nrows):
#     a=sheet.row_values(i)
#     c.append(a)
#     if i==0:
#         aa.execute('create table ff({} char(10),{} char(10),{} char(10),{} char(10));'.format(c[0][0],c[0][1],c[0][-2],c[0][-1]))
#     else:
#         aa.execute('insert into ff values("{}","{}","{}","{}");'.format(c[i][0],c[i][1],c[i][-2],c[i][-1]))

