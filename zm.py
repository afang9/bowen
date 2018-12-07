#/usr/bin/env python
#--*-- coding:utf-8 -*-
# import day1
# from day1 import jiu9

# b="""meiliyoudafang"""
# f=open(r'C:\Users\旭方\Desktop\bb.txt','a',encoding='utf-8')
# f=open(r'C:\Users\旭方\Desktop\bb.txt','a',encoding='utf-8')
# f.write('456')
# f.write('ffff'+'\n')
# f.write('ddddd')
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline()[1:5])
# f.close()



# f=open(r'C:\Users\旭方\Desktop\mm.txt','w',encoding='utf-8')
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         f.write('{}*{}={}'.format(i,j,i*j)+'\t')
#         if i==j:
#             f.write('\n')
# f.close()

# with open(r'C:\Users\旭方\Desktop\dadada.jpg','rb') as f:
#     a=f.read()
#     print(a)
# with open('wewe.jpg','wb') as f:
#     f.write(a)

# a=open(r'C:\Users\旭方\Desktop\dadada.jpg','rb')
# b=a.read()
# a.close()
# print(b)
# a=open('da.jpg','wb')
# a.write(b)
# a.close()


# with open('bb.txt','r',encoding='utf-8') as f:
#         a=f.readlines()
#         print(len(a))
# for i in a:
#     if i=='\n' or i[0]=='#':#i.startswith('#')
#
#         a.remove(i)
#     print(len(a))

# for i in range(10):
#     with open('b{}.txt'.format(i),'w+',encoding='utf-8') as f:
#             for j in range(10):
#                 f.write('wewe'+'\n')




# try:
#     a='ninini'
#     print(a+'1')
# # except:                                      #=except:
# #     print(123)
# except TypeError as c:
#     print(c)
#     print('hello')
# else:
#     print('wanmei')
# finally:
#     print('yyyyy')

# A=13215                                    #/A=13213
# if A==13213:
#     raise TypeError('bao cuo ba!')
# print(A+1)                                 #直接会触发错误


#
# day1.jiujiu(1,10)


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

# class shuzi():
#     def jiujiu(self):
#         print(self.__shishu)
#         b=self.zhishu()
#         a=b+1
#         print(b)
#     def __zhishu(self):
#         b=123
#         return b
# e=shuzi()
# e.jiujiu()
# class dd():
#     def aaa(self):
#         print(123)
#     pass
# d=dd()
# d.jiujiu()
# class sdf(shuzi,dd):
#     pass
# sdf=sdf()
# sdf.aaa()
# class chongxie(shuzi,dd):
#     def aaa(self):
#         s=0
#         for i in range(5):
#             s+=i
#         print(s)
# aa=chongxie()
# aa.__jiujiu()













# class banji():
#     name = '小明'
#     nianji=10
#     def __init__(self,a,b):
#         self.name=a
#         self.nianji=b
#     def stu(self,c):
#         print('hello %s,你%d级'%(self.name,self.nianji),34)
#     def stu1(self):
#         print('hello %s,有18岁了,能打h个'%(self.name,self.nianji))
# # aa=banji('明明',10)
# # aa.stu(3)
# # aa.stu1()
# bb=banji('灰灰')
# bb.stu()
# bb.stu1()











# class zhihui():
#     def zhishu(self,x,y):
#         s=0
#         for i in range(x,y):
#             for j in range(x,i):
#                 if i%j==0:
#                     break
#             else:
#                 s+=i
#         print(s)
#     def huiwen(self,a):
#         b=a[::-1]
#         if a==b:
#             print('huiwen')
#         else:
#             print('bushihuiwen')
# aa=zhihui()
# aa.zhishu(2,100)
# bb=zhihui
# aa.huiwen('qweewq')




















#
# import pymysql
# abc=pymysql.connect(host='192.168.0.22',
#                     port=3306,
#                     user='root',
#                     password='qwert',
#                     charset='utf8',
#                     db = 'sjk')
# aaa=abc.cursor()
# # # aaa.execute('create database sjk;')
# aaa.execute('use sjk;')
# # aaa.execute('create table biao3 (姓名 char(255),年龄 int,班级 char(255));')
# # print(aaa.fetchmany(2))
# list5 = ['小明',1,'班级']
# for i in range(30):
#     aaa.execute('insert into biao3 values ("{}",{},"{}");'.format(list5[0],list5[1]+i,'{}'.format(i)+list5[2]))
#     abc.commit()
# a=aaa.execute('select * from biao3;')
# for i in a:
#     print(i)
# ccc=abc.cursor()
# ccc.execute('select * from biao3;')
# shuju=ccc.fetchall()
# print(shuju)
# ccc.execute('desc biao3;')
# biaotou=ccc.fetchall()
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i==len(biaotou)-1:
#             f.write(biaotou[i][0])
#         else:
#             f.write(biaotou)


