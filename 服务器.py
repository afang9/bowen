# import xlwt
# f=xlwt.Workbook('utf-8')
# ab=f.add_sheet('py操作xls')
# for i in range(10):
#     for j in range(5):
#         ab.write(i,j,'大头皮鞋')
# f.save('ly.xls')
# import xlwt
# f=xlwt.Workbook('utf-8')
# ab=f.add_sheet('py操作')
# for i in range(9):
#     for j in range(5)
#         ab.write(i,j,'liudatou')
# f.save('mm.xls')
# import xlwt
# f=xlwt.Workbook('utf-8')
# ab=f.add_sheet('大头')
# for i in range(9):
#     for j in range(10):
#         ab.write(j,i,'xiaohuozo')
# f.save('2.xls')
import os
# a=os.popen('ping  192.168.0.22')
# print(a.read())
# print(os.getcwd())
# os.chdir(r'E:\py')
# print(os.getcwd())
# for i in range(3,10):
#     os.mkdir(r'{}'.format(i))
#     a = r'{}'.format(i)
#     with open(r"{}/{}.txt".format(a,i),'w',encoding='utf-8') as f:
#         for k in range(5):
#             f.write('qwe'+'\n')
#     os.remove(r"{}/{}.txt".format(a,i))
#     os.rmdir('{}'.format(i))
# import xlwt
# f=xlwt.Workbook('utf-8')
# ab=f.add_sheet('python操作')
# for i in range(4):
#     for j in range(3):
#         ab.write(j,i,'学长克鲁')
# f.save('mm.xls')
# import xlrd
# f=xlrd.open_workbook('mm.xls')
# sheet=f.nsheets
# # print(sheet)
# sheet=f.sheets()[0]
# # print(sheet)
# a=sheet.nrows
# # print(a)
# g=[]
# for i in range(a):
#     # b=sheet.row_values(i)
#     # print(b)
#     c=sheet.ncols
#     # print(c)
#     for j in range(c):
#         # d=sheet.col_values(j)
#         # print(d)
#         f=sheet.cell(i,j).value
#         # print(f)
#         g.append(f)
# print(g[0])
# import xlrd
# f=xlrd.open_workbook('mm.xls')
# sheet=f.nsheets
# print(sheet)
# print(f.sheet_names())
# sheet=f.sheets()[0]
# print(sheet.nrows)
# print(sheet.row_values(0))
# print(sheet.ncols)
# print(sheet.col_values(0))
# print(sheet.cell(0,0).value)
# print(f.sheet_by_name('python操作'))
# print(sheet)
# print(f.sheet_names())
import xlrd
from xlutils.copy import copy


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',233)
# s.bind(a)
# s.listen(123)
# while True:
#     a,b=s.accept()
#     a.recv(1024)
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='welcome'
#     a.send(reg.encode('utf=8'))


# import socket                                     #UDP
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',200)
# s.bind(a)
# # s.listen(3)
# while True:
#     a,b=s.recvfrom(1024)#接收数据   a，客户端发送的请求数据。b,客户端的IP地址和端口号
#     print(a.decode('utf-8'))
#     print(b)
#     #发送响应数据
#     msg=input('请开始话题！')
#     s.sendto(msg.encode('utf-8'),b)


# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # a=('0.0.0.0',200)
# # s.bind(a)
# # # print(s)
# # s.listen(4)
# # while True:
# #     a,b=s.accept()
# #     # print(a)
# #     print(b)
# #     msg=a.recv(1024)
# #     print(msg.decode('utf-8'))
# #     reg='星空下无敌！'
# #     a.send(reg.encode('utf-8'))

# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # a=('0.0.0.0',300)
# # s.bind(a)
# # s.listen(4)
# # while True:
# #     a,b=s.accept()
# #     msg=a.recv(1024)
# #     print(msg.decode('utf-8'))
# #     reg='??????'
# #     a.send(reg.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',200)
# s.bind(a)
# s.listen(4)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='????'
#     a.send(reg.encode('utf-8'))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',200)
# s.bind(a)
# s.listen(4)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='戒骄、戒躁'
#     a.send(reg.encode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('127.0.0.1',200)
# s.bind(a)
# s.listen(6)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='他强由他强，明月照大江！'
#     a.send(reg.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('127.0.0.1',200)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     msg='guawawa'
#     s.sendto(msg.encode('utf-8'),b)

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',200)
# s.bind(a)
# s.listen(4)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='上九天揽月，下五洋捉鳖'
#     a.send(reg.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',200)
# s.bind(a)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     aa='错不可及的思想，才是和别人差距最大的原因'
#     a.send(aa.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     reg='不是从心，难得初心'
#     s.sendto(reg.encode('utf-8'),b)

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     reg='执着之人，必有可恨之处！'
#     s.sendto(reg.encode('utf-8'),b)

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     meg='想起你，又想忘记你，忘却你，心里又恋着你！'
#     s.sendto(meg.encode('utf-8'),b)
# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # a=('0.0.0.0',100)
# # s.bind(a)
# # while True:
# #     a,b=s.recvfrom(1024)
# #     print(a.decode('utf-8'))
# #     reg='自动化'
# #     s.sendto(reg.encode('utf-8'),b)

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',100)
# s.bind(a)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='陌生的声音！'
#     a.send(reg.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     reg='千篇一律的皮囊！'
#     s.sendto(reg.encode('utf-8'),b)
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.91',100))
# reg='dedededdddd'
# s.send(reg.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     reg='事无忧，则前尘忧！'
#     s.sendto(reg.encode('utf-8'),b)
# import pymysql
# ab=pymysql.connect(host='192.168.0.22',user='root',password='qwert',port=3306,charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# aa.execute('desc ss;')
# a=aa.fetchall()
# # print(a[3][0])
# aa.execute('select * from biao1;')
# b=aa.fetchall()
# q=[]
# for k in b:
#     q.append(k)
#     print(q)
# with open('erer.txt','w',encoding='utf-8') as f:
#     for i in range(len(a)):
#         # if i==len(a)-1:
#         f.write(a[i][0]+' ')
#     f.write('\n')
#         # else:
#         #     f.write(a[i][0])
#     for j in range(len(b)):
#         for l in range(len(q[0])):
#             print(j)
#             # f.write('{},{},{},{}'.format(k[0],k[1],k[2],k[3])+'\n')
# import os
# print(os.rename('练习.py','服务器.py'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',100)
# s.bind(a)
# s.listen(45)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='fg'
#     a.send(reg.encode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     reg='dsfs'
#     s.sendto(reg.encode('utf-8'),b)




















