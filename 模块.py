import pymysql
import xlwt
import xlrd
#excel表格的追加
import xlrd
from xlutils.copy import copy
import paramiko
import smtplib
import email.mime.text
import email.mime.multipart
import time
# abc=pymysql.connect(host='192.168.0.22',
# #                     port=3306,
# #                     user='root',
# #                     password='qwert',
# #                     charset='utf8')
# # aaa=abc.cursor()
# aaa.execute('create database stu;')
# aaa.execute('show databases;')
# print(aaa.fetchall())
# aaa.execute('use stu;')
# aaa.execute('create table syu(学号 char(10),姓名 char(10),年龄 char(10),班级 char(10));')
# aaa.execute('desc syu;')
# print(aaa.fetchmany(3))
# print(aaa.fetchall())
# list3=[2001,'大郭',1,'班']
# for i in range(5):
#     aaa.execute('insert into syu values({},"{}",{},"{}");'.format(list3[0]+i,list3[1],list3[2]+i,'{}'.format(i)+list3[3]))
#     abc.commit()
# aaa.execute('select * from syu;')
# for i in aaa.fetchall():
#     print(i)
# aaa.execute('select * from syu')
# shuju=aaa.fetchall()
# print(shuju)
# aaa.execute('desc syu;')
# biaotou=aaa.fetchall()
# print(biaotou)
# print(type(biaotou),len(biaotou))
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i==len(biaotou)-1:
#             print("换行")
#              # f.write(biaotou[i][0]+'\n')
#         else:
#             f.write(biaotou[i][0]+',')
#     for j in shuju:
#         print(j)
#         f.write('{},{},{},{}'.format(j[0],j[1],j[2],j[3])+'\n')










import os
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
# for i  in os.listdir():
#     if os.path.isfile(i):
#         print(i)
# print()
# for i in os.listdir():
#     if os.path.isdir(i):
#         print(i)

# os.chdir(r'E:\QQ\1241378256\FileRecv')
# e=os.listdir(r'E:\QQ\1241378256\FileRecv')
#
# print(e)
# a=0
# b=0
# for i in e:
#     if os.path.isfile(i):
#         a+=1
#     elif os.path.isdir(i):
#         b+=1
# print(a,b)


# a=[x for x in e  if os.path.isfile(x)]
# b=[y for y in e  if os.path.isdir(y)]
# print(len(a),len(b))

import xlwt
# #打开一个空白文件，如果没有命名编码方式需在括号内加入:
# f=xlwt.Workbook()
# #添加一个标签页，括号中写标签页的名称
# sheet=f.add_sheet('python操作excel表格')
# #x写入数据：
# #第一个数字代表多少行，第一行从0开始
# #第二个数字代表多少列，第一列从0开始
# #第三个字符串代表写入内容
# sheet.write(0,1,'姓名')
# #保存文件
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

f=xlwt.Workbook()
af =f.add_sheet('python操作stu1')
af.write(0,0,'学号')
af.write(0,1,'姓名')
af.write(0,2,'年龄')
af.write(0,3,'班级')
af.write(0,4,'成绩')
d=[2000,'小张',22,'班',70]
for i in range(10):
    for j in range(5):
        af.write(i+1,j,d[j])
f.save('text.xls')




#练习
# f=xlrd.open_workbook('text.xls')
# sheet=f.nsheets
# print(sheet)
# sheet=f.sheets()[0]
# print(sheet.nrows)
# a=sheet.nrows
# for i in range(a):
#     print(sheet.row_values(i))
# print(sheet.ncols)
# print(sheet.col_values(0))
# print(sheet.cell(0,0).value)
#
# print(f.sheet_names())
# sheet=f.sheet_by_name('python操作stu1')


# f=xlrd.open_workbook('text.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(11,5,'eieiei')
# new_f.save('text.xls')
# f=xlrd.open_workbook('text.xls')
# sheet=f.nsheets
# print(sheet)
# sheet=f.sheets()[0]
# print(sheet)
# print(sheet.nrows)
# print(sheet.row_values(7))
# print(sheet.ncols)
# print(sheet.col_values(2))
# print(sheet.cell(2,4).value)

# f=xlrd.open_workbook('text.xls')
# # print(f.sheet_names())
# sheet=f.sheet_by_name('Sheet1')

# f=xlrd.open_workbook('Sheet1')
# new_f=copy(f)
# sheet=new_f.get_sheet(1)

# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.0.22',
#                port=22,
#                username='root',
#                password='qwert')
# #执行命令 产生三个结果
# while True:
#     a=input('请输入有结果的命令：')
#     if a == 'exit':
#         break
#     else:
#         stuin,stuout,stuerr=ssh123.exec_command(a)#只能输入有结果的命令
# # 第一个变量：执行的命令，输入
# # 第二个变量：命令的结果，输出
# # 第三个变量：命令的报错
#     print(stuout.read().decode())

# ssh123.close()#断开连接

#创建一个传输通道     只能接收元组
# ssh122=paramiko.Transport(('192.168.0.22',22))
# ssh122.connect(username='root',password='qwert')
# #传输文件使用sftp协议，  创建一个sftp的实例
# sftp=paramiko.SFTPClient.from_transport(ssh122)
# #get 是从Linux下载文件到本地
# # sftp.get('while.sh','./aaa.sh')
# #put是从本地向Linux上上传文件
# sftp.put('./day1.py','/etc/aaa.py')
# sftp.close()




# sender='lxf37727@163.com' #发送者
# recver=['m15037109541@163.com','zhengbo19960406@163.com']#接受者
# server='smtp.163.com'#163的服务器地址
# # server='smtp.qq.com'
# password='qwert124'       #授权码
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# #发件人
# message['from']=sender
# #收件人
# # message['to']=recver
# message['to']=','.join(recver)
# #主题
# message['subject']='python daungfuang'
# #正文
# text="""
# daung!daung!daung!你是卖货的小皮凉！！！！！！！
# """
# #处理文本信息
# text=email.mime.text.MIMEText(text)
# #将处理后的信息添加到邮件里
# message.attach(text)
# #添加附件；处理附件：以二进制的方式读取文件
# aa1=email.mime.text.MIMEText(open(r'C:\Users\旭方\Desktop\timg.jpg','rb').read(),'base64','utf-8')
# aa1["Content-Type"]='application/octet-stream'
# aa1["Content-Disposition"]='attachment;filename="timg.jpg"'
# message.attach(aa1)
# #定义服务器和端口
# smtp123=smtplib.SMTP_SSL(server,465)
# #登录服务器
# smtp123.login(sender,password)
# #发送邮件
# smtp123.sendmail(sender,recver,message.as_string())
# #断开连接
# smtp123.close()

#相当于winscp  windows\linux互相换文件
# ssh122=paramiko.Transport(('192.168.0.22',22))
# ssh122.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(ssh122)
# sftp.get('while.sh','./ee.sh')
# sftp.put('./zm.py','/home/aa.py')
# sftp.close()

# print(time.time())
# print(time.localtime(12344324341.3243544564565465))
# print(time.strftime('%Y %m %d %H-%M-%S %A',time.localtime()))

# a=time.strptime('2044 10 20','%Y %m %d')
# # print(time.strptime('2044 10 20','%Y %m %d'))
# print(time.mktime(a))
# # time.sleep(3)
# # print('www')
# a=input('请输入年-月-日')
# a=a.split('-')
# for i,j in enumerate(a):
#     a[i]=int(j)
# if (a[0]%4==0and a[0]%100!=0) or a[0]%400==0:
#     print('{}是闰年'.format(a[0]))
# else:
#     print('不是闰年')
# c=time.strptime('{} {} {}'.format('a[0],a[1],a[2],%Y %m %d'))
# print(c)
# print('今天是周{}'.format(c[-3]+1))
# print('今天是一年中的第{}天'.format(c[-2]))



# os.rename('购物车.py','模块1.py')
#txt.提取到xls,一样
# with open('a.txt','r',encoding='utf8') as f:
#     a=f.read()
# t=xlwt.Workbook()
# ad=t.add_sheet('python操作excel表格')
#
#     ad.write(0,0,)
# t.save('tee1.xls')


#相当于winscp  windows\linux互相换文件
# ssh122=paramiko.Transport(('192.168.0.22',22))
# ssh122.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(ssh122)
# sftp.get('while.sh','./ee.sh')
# sftp.put('./zm.py','/home/aa.py')
# sftp.close()

# ssh12=paramiko.Transport(('192.168.0.22',22))
# ssh12.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(ssh12)
# sftp.get('while.sh','./ee.sh')
# sftp.put('./zm.py','/home/ff.py')
# sftp.close()
import xlrd
from xlutils.copy import copy
import xlrd
from xlutils.copy import copy
import xlrd
from xlutils.copy import copy
# ssh1=paramiko.Transport(('192.168.0.22',22))
# ssh1.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(ssh1)
# sftp.get('','')
# sftp.put('','')
# sftp.close()
#
# import xlrd
# from xlutils.copy import copy
# sshxx=paramiko.Transport(('192.168.0.22',22))
# sshxx.connect(username='root',password='qwert')
# sshxx=paramiko.Transport(('192.168.0.22',22))
# sshxx.connect(username='root',password='qwert')
# sshxx=paramiko.Transport(('192.168.0.22',22))
# sshxx.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(sshxx)
# sftp.get('','')
# sftp.put('','')
# sftp.close()
#
#
# import xlrd
# from xlutils.copy import copy
# sshx=paramiko.Transport(('192.168.0.22',22))
# sshx.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(sshx)
# sftp..get('','')
# sftp.put('','')
# sftp.close()
#
# import xlrd
# from xlutils.copy import copy
# ssh2=paramiko.Transport(('192.168.0.22'22))
# ssh2.connect(username='root',password='qwert')
# sftp=paramiko.SFTPClient.from_transport(ssh2)
# sftp.get('','')
# sftp.put('','')

# import paramiko
# sshq=paramiko.SSHClient()
# sshq.set_missing_host_keypolicy(paramiko.AutoAddPolicy())
# sshq.connect(hostname='192.168.0.22',port=22,username='root',password='qwert')
# a,bout,c=sshq.exec_command('ls -al')
# print(bout.read().decode())
# sshq.close()
#
# import paramiko
# sshq=paramiko.SSHClient()
# sshq.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# sshq.connect(hostname='192.168.0.22',port=22,username='root',password='qwert')
# a,bout,c=sshq.exec_command('ls -al')
# print(bout.read().decode())
# sshq.close()
#
# import paramiko
# sshq=paramiko.SSHClient()
# sshq.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# sshq.connect(hostname='192.168.0.22',port=22,username='root',password='qwert')
# a,bout,c=sshq.exec_command('ls -al')
# print(bout.read().decode())
# sshq.close()
