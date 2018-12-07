# import pymysql                                                #mysql导入txt
# ab=pymysql.connect(host='192.168.0.22',user='root',port=3306,charset='utf8',password='qwert')
# aa=ab.cursor()
# aa.execute('use stu;')
# aa.execute('desc biao1;')
# a=aa.fetchall()
# aa.execute('select * from biao1;')
# b=aa.fetchall()
# print(len(b))
# c=[]
# for k in b:
#     c.append(k)
# print(c)
# with open('asd.txt','w+',encoding='utf-8') as f:
#     for i in range(len(a)):
#         f.write('{}'.format(a[i][0]))
#         f.write(',')
#     f.write('\n')
#     for h in c:
#         print(h)
#         for j in range(len(c[0])):
#         # print(c[0])
#             f.write('{}'.format(h[j]))
#             f.write(',')
#         f.write('\n')
# import pymysql                                        #TXT导入MySQL
# ab=pymysql.connect(host='192.168.0.22',port=3306,password='qwert',user='root',charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# c=[]
# with open('asd.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
#     # print(len(a))
# for i in a:
#     b=i.replace(',\n','').split(',')
#     # print(len(b))
#     c.append(b)
# print(c)
#
# for j in range(len(c)):
#     if j == 0:
#         pass
#         # aa.execute('create table tt ({} char(10),{} char(10),{} char(10),{} char(10));'.format(c[j][0],c[j][1],c[j][-2],c[j][-1]))
#     else:
#         aa.execute('insert into tt values("{}","{}","{}","{}");'.format(c[j][0],c[j][1],c[j][2],c[j][3]))
# import xlwt                               #TXT导入xls
# c=[]
# with open('erer.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# for k in a:
#     b=k.replace('\n','').split(',')
#     c.append(b)
# g=xlwt.Workbook('utf-8')
# sheet=g.add_sheet('txt导xls')
# for i in range(len(c)):
#     for j in range(len(b)):
#         sheet.write(i,j,c[i][j])
# g.save('ff.xls')
# import xlrd                                               #xls导入TXT
# f=xlrd.open_workbook('ff.xls')
# print(f.nsheets)
# print(f.sheet_names())
# sheet=f.sheets()[0]
# with open('vb.txt','w',encoding='utf-8') as f:
#     for i in range(sheet.nrows):
#         for j in range(sheet.ncols):
#             a=sheet.row_values(i)
#             f.write('{}'.format(a[j])+',')
#         f.write('\n')
# import pymysql                                        #MySQL导入xls
# ab=pymysql.connect(host='192.168.0.22',password='qwert',user='root',charset='utf8',port=3306)
# aa=ab.cursor()
# aa.execute('use stu;')
# aa.execute('desc biao1;')
# a=aa.fetchall()
# print(a)
# aa.execute('select * from biao1;')
# b=aa.fetchall()
# print(b)
# with open('ig.txt','w',encoding='utf-8')as f:
#     for i in range(len(a)):
#         f.write('{}'.format(a[i][0]+','))
#     f.write('\n')
#     for k in b:
#         for j in range(len(b[0])):
#             f.write('{}'.format(k[j]))
#             f.write(',')
#         f.write('\n')

# import pymysql                                                 #sql导入xls
# import xlrd
# ab=pymysql.connect(host='192.168.0.22',password='qwert',port=3306,user='root',charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# f=xlrd.open_workbook('rrr.xls')
# print(f.sheet_names())
# sheet=f.sheets()[0]
# c=[]
# for i in range(sheet.nrows):
#     a=sheet.row_values(i)
#     c.append(a)
#     if i==0:
#         pass
#             # aa.execute('create table rr ({} char(10),{} char(10),{} char(10),{} char(10),{} char(10),{} char(10));'.format(a[0],a[1],a[2],a[3],a[4],a[5]))
#     else:
#         aa.execute('insert into rr values("{}","{}","{}","{}","{}","{}");'.format(a[0],a[1],a[2],a[3],a[-1],a[-2]))
# import pymysql                                     #MySQL导入xls
# import xlwt
# ab=pymysql.connect(host='192.168.0.22',password='qwert',user='root',port=3306,charset='utf8')
# aa=ab.cursor()
# aa.execute('use stu;')
# aa.execute('desc biao1;')
# a=aa.fetchall()
# aa.execute('select * from biao1;')
# b=aa.fetchall()
# print(b[0])
# f=xlwt.Workbook()
# ad=f.add_sheet('mysql导入xls')
# for i in range(len(b)):
#     for j in range(len(b[0])):
#         if i==0:
#             ad.write(i,j,a[j][0])
#         else:
#             ad.write(i,j,b[i][j])
# f.save('cs.xls')
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',200)
# s.bind(a)
# s.listen(4)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='呱唧呱唧'
#     a.send(reg.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',100)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     reg='...'
#     a.sendto(reg.decode('utf-8'),b)

# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender='lxf37727@163.com'
# recver='1241378256@qq.com'
# server='smtp.163.com'
# password='qwert124'
# message=email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['to']=recver
# message['subject']='lalalal'
# text="""duangdaungdaung!"""
# text=email.mime.text.MIMEText(text)
# message.attach(text)
# smtp1=smtplib.SMTP_SSL(server,465)
# smtp1.login(sender,password)
# smtp1.sendmail(sender,recver,message.as_string())
# smtp1.close()

# class Zhi_shu():
#     def zhishu(self):
#         sum=0
#         for i in range(2,100):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 sum+=i
#         print(sum)
#     def jiujiu(self):
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 print('{}*{}={}'.format(i,j,i*j),end='\t')
#             print()
#     def huiwen(self,a):
#         b=a[::-1]
#         if a==b:
#             print('y')
#         else:
#             print('n')

# zj=Zhi_shu()
# zj.zhishu()
# zj.jiujiu()
# zj.huiwen('qweew')


import os
# os.chdir(r'E:\QQ\1241378256\FileRecv')
# print(os.getcwd())
# os.chdir(r'd:')
# print(os.getcwd())
# os.chdir(r'c:')
# print(os.getcwd())
# os.mkdir(r'e:\py\ff')
# os.makedirs(r'e:\py\xiao\xue\jian\jia\zhang')
# print(os.getcwd())
# with open(r'e:\py\xiao\xue\jian\jia\zhang\a.txt','w',encoding='utf-8')as f:
#     f.write('无烟')
# os.makedirs(r'as\ad')
# os.remove(r'e:\py\xiao\xue\jian\jia\zhang\a.txt')
# os.removedirs(r'as\ad')
# os.rename('爬虫，动态获取.py','练习.py')
# os.rename('脚本联系.py','服务器.py')
# print(os.path.split(r'r:\m.py'))
# print(os.path.split(r'd:\y\df\s.xls'))
# print(os.path.splitext(r'e:\df.py'))
# print(os.listdir(r'e:'))
# print(len(os.listdir(r'd:')))
# print(os.path.isfile(r'zm.py'))
os.rename('对文件xlsmysql.py','文件转入转出.py')







# class shuzi():
#     def jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s*=i
#             d+=s
#             return d
#     def zhishu(self):
#         b=self.jiecheng()           #self  内置类的实例化 方便调用
#         s = 0
#         for i in range(2,b+1):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 s+=i
#         print(s)
#

# h=shuzi()
# h.zhishu()