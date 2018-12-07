#/usr/bin/env python
# -*- coding:utf-8 -*-
# import random

# 输出 等同于 echo 格式：print()
#print('sdas')
#print(123)
#print('哇哈哈哈','ssss','xiaozhu','wukong')

# 输入 从键盘上输入 等同于 read -p 提示 input(提示)
#变量名 = input('请输入成绩:')
#print(变量名)

# 变量 变化的量 常量
# 定义变量的格式：变量名=数据

#a,b,c=134,'aaa','中国'
#print(a,b,c)
# a=345
# b=it(type(b))
# a=True
# print(type(a))
# a='123 4'
# a='qwer'
# print(a[::-3])
#
# a='adaf'
# b=a.upper()
# print(b)

#a.append('assd')
#print(a)
# b=a
# a.append(b)
# print(a)
# a[4][[1]].append('aaa')
# print(a)
# a.insert(2,'ddd')
# print(a)
# c=a.index(4)
# print(c)

# a.insert(5,'fff')????////////////??????
# print(a)
# a=(2)
# print(type(a))
# a=('s','sf','fg',23)
#b=['asd','sfds','d',23,675,'ssss']
#print(a+b)
# a[2]=1000
# b[2]=1000
#print(a)
#b=input('请输入')
#print(type(b))
#
# a.reverse()
# b.reverse()
# print(a)
# a=[32,543,645,4356,423,4]
# a.sort()
# print(a)
# #a.sort(reverse=True)
# a.sort()
# a.reverse()
# print(a)
# import copy

# f=copy.deepcopy(a)
# a.append(100)
# a[5].append(100)
# print(f)
# print(a)
# b=['sfs','sdgf',4]
# a=['a','2434','qwe',4,'wwe',b]
# # a.extend(b)
# # print(a)
# # print(b*2) #输出列表两次
# print(a+b)#合并组合列表
# a={'name':'小明','sex':'男','age':[20,32,45]}
# a['age'][2]='小p'
# a['name']='花花'
# print(a)

# c=a|b
# print(c)
# d=a&b
# print(d)
# f=a-b
# print(f)
#
# b[6][4].insert(1,'aaa')
# print(b)
# a=' a b c ,b ef aab '
# b=a.replace(',','')
# b=a.split(',')
# print(b)
# a=[12,23,34,23,12,4,4,44]
# # b=[55,6,12,a]
# # # c=set(a)
# # # print(type(c))
# # c=set(a)
# # e=list(c)
# # e.sort()
# # print(e)
# # e.reverse()
# # print(e)
# a=['saa','asd','vcc','cbc']
# print('vcc' not in a)
# a=3+3
# b=5
# a+=b
# if a > 30:
#     print('hhh')
# else:
#     print('mmm')
# a=input('请输入成绩：')
# b=int(a)
# if  b >90 and b<=100:
#     print('优秀')
# elif b >80 and b<=90:
#     print('良好')
# elif b >70 and b<=80:
#     print('及格')
# elif b< 60:
#     print('菜鸡')
# e=input('请输入字符串：')
# # if e.startswith('a'):
# #     if e.endswith('c'):
# #        print('hello world')
# #     else:
# #        print('hello')
# # elif e.endswith('c'):
# #        print('word')
# # else:
# #     print(123)
# a='sdsdfkdljjdgfgm'
# a.startswith('a')
# print(a)

# d=input('请输入元素：')
# e=d.split(',')
# e.sort()
# a,b,c=int(e[0]),int(e[1]),int(e[-1])
# if a + b > c:
#     if a**2+b**2 < c**2:
#         print('钝角')
#     elif a**2+b**2==c**2:
#         print('直角')
#     elif a**2+b**2>c**2:
#         print('锐角')
# else:
#    print('并不是三角形')
# a=[1,2,2,3,4,5,6,5,3,0]
# b=set(a)
# print(b)


# print(a.replace('a',''))
# b='hello {},我很{}'
# print(b.format('老哥','慌!'))
# print(b.format('我很好','hao'))
# a='sffg'
# c='-'
# print(c.join(a))
# a=' aas,DD SA, fs Daf dSf,das '
# print(a.split(', '))

# a=['fddsa','dsf','sgcx','fgf',['vcb',143,'234','d',4],56]
# b=['df','g',a]
# b.insert(2,'sss')
# print(b)
# a={'name':'xaio','sex':'男','age':23}
# for i,j in a.items():
#     print(i,j)
# a=0
# # b=0
# # for i in range(1,100,2):
# #     a+=i
# # for j in range(2,100,2):
# #     b+=j
# # print(a-b)
# b=['dfvcx','dfh','vbnvc',['dfgd','fgdf'],3432]
# # a=['df','fg','gfg',23,b]
# # for i in enumerate(a[4]):
# #     print(i)
# # for c in enumerate(a):
# #     print(c)


# a=['电脑','计算机','mp3']
# for i,j in enumerate(a):
#     print(i+1,j)
# c=input('请输入商品号:')
# b=int(c)
# print(a[b-1])
# b=0
# for i in range(1,100):
#     if i%2==0:#if i%2!=0:
#         b-=i  #b+=i
#     else:
#         b+=i  #b-=i
# print(b)
#
# print(a)

# for j in range(3):
#     for i in range(2):
#         for k in range(3):
#             print('nihao//',end=',')
# for i in range(1,10):
#     for j in range(1,10): #for j in range(1,i+1)
#         if j<=i:            #
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
# for i in range(1,10):
#     if i==6:
#         continue
#     else:
#         print(i)

# a=['dfsd','fdg','232']
# for i in a:
#     if len(i)==2:
#         break
#         print('没有')
# else:
#     print('完美')

# a = random.randrange(1,10)
# print(a)
# for i in range(1,10):
# #    for j in range(3):
#         if i==a:
#             print(a)
#             break
#         if i<a:
#             print('还大')
#         if i>a:
#             print('还小')
# else:
#     print('cai')
# b=0
# for i in range(2,100):
#     for j in range(2,100):
#         print()
#              if j==i:
#                 b+=i
#     print(b)

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         print(n, ' 是质数')

# for i in range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()

# for i in range(2,101):
#     a=0
#     for j in range(2,101):
#         if i%j==0:
#            break
#     else:
#         a+=i
#     print(a)

# a=input('请输入一个数')
# c=int(a)
# e=1
# s=0
# for i in range(1,c+1):
#         e*=i
#         s+=e
# print(s)

# a=1
# s=0
# while a<=100:
#     s+=a
#     a+=1
# print(s)

# a=0
# for i in range(1,101):
#     a+=i
# print(a)
# a=random.randrange(1,10)
# c=input('请输入一个数：')
# b=int(c)
# while b=a:
#     print(a)
# while b<a:
#     print('还大')
# while b>a:
#     print('还小')

# a=1
# s=0
# while a<=9:
#     s+=a
#     a+=1
#     b=1
#     if s<=a:
#          print('{}*{}={}'.format(s,a,s*a),end='\t')
#          b+=1
# print()


# a=1
# b=1
# while a<10:
#     while b<=a:
#         print('{}*{}={}'.format(a,b,a*b),end='\t')
#         b+=1
#     print()
#     a+=1

# a=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a+=i
# print(a)

# while True:         #计算平均值
#     a=input('请输入一组数:')
#     if a=='exit':
#         break
#     b=a.split(',')
#     c=len(b)
#     for i,j  in enumerate(b):
#         b[i]=int(j)
#     x=(sum(b)/c)
#     print(x)
#     for k in b:
#         if k<x:
#             print(k)



# a=['12','3','3']
# c=len(a)
# for i,j in enumerate(a):
#     a[i]=int(j)
# print(sum(a)/c)


# i=1
# while i <10:
#         j=1
#         while j<=i:
#                 print('{}*{}={}'.format(j,i,j*i),end='\t')
#                 j+=1
#         print()
#         i+=1

# def zhishu():
#         s=0
#         for i in range(2,101):
#                 for j in range(2,i):
#                         if i%j==0:
#                                 break
#                 else:
#                         s+=i
#                 return s
# print(__name__)
# if __name__!='__main__':
#         print('1211212')
#         print(zhishu())

# a=input('请输入一个数：')     #阶乘之和
# b=int(a)
# s=0
# e=1
# for i in range(1,b+1):
#         e*=i
#         s+=e
# print(s)

# a=input('请输入一组数：')
# for i in range(a):
#     if i==a:
#         print()

# s=0
# i=2
# while i<101:
#     j=2
#     while j<i-1:
#         if i%j==0:
#             break
#             j+=1
#     else:
#         s+=i
#         i+=1
#         print(s)

# a='1223243435'            #不用int将什么变为整数
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for k in range(10):
#         if str(k)==j:
#             s+=k*10**i
#             break
#         print(s[::-1])

# a='qweewq'         #回文
# b=len(a)//2
# for i in range(b):
#     if a[i]!=a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')

# a=input('请输入一组数字：')    #回文
# # b=a.split(',')
# # c=b[::-1]
# # if c==b:
# #     print('yes')
# # else:
# #     print('no')
#
# a=input('请输入一组数字:')
# b=a.split(',')
# c=a.index(max(a[0]))                  ?????????????????????
# d=a.index(min(a[-1]))
# b[d],b[0]=b[0],b[d]
# b[c],b[-1]=b[-1],b[c]
# print(b)

# a=[23,543,3423,3434]
# c=a.index(max(a))
# b=a.index(min(a))
# # print(c)
# # print(b)
# c=a.copy()
# c.sort()
# e=a.index(c[0])
# n=a.index(c[-1])
# a[n],a[0]=a[0],a[n]
# # a[e],a[-1]=a[-1],a[e]
# print(a)

# a=['23','543','3423','3434']
# c=a.copy()
# c.sort()
# print(c)
# b=c[-1]
# print(b)
# r=[12,12334,34,34545,4560,0]
# g=r.copy()
# g.sort()
# print(g)

# def jiu9():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#         print()
#         # return 123
# jiu9()


# def fff(**args):
#     print(args)
# # fff('4,,3,,,,,,5',344,{'name':123},(1,2),['ddfd','gfdgd','dfgdfgd'])
# fff(qwe=123,qwe='小p')

# def jiu9(*x):
#     a=
#     for i in range(x):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#         print()
# jiu9(3,4,5)
# a=(1,2,3)
# b=int(a[0])
# print(b)

# a=input('请输入一串数字：')
# b=a.split(',')
# for i,j in enumerate(b):
#     if b[i]==j:
#         print(j)

# a=input('请输入一组数：')         #去重
# c=a.split(',')
# b=[]
# for i in c:
#         b.append(i)
#         e=set(b)
# print(e)

#     x=input(':::')
#     b=x.split(',')
#     for i in b:
#         if b.count(i)>1:
#             for j in range(b.count(i)-1):
#                 b.remove(i)
#     print(b)



# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('请输入数'))
# f=''
# while True:
#      c=b%16
#      b=b//16
#      f=f+a[c]
#      if b==0:
#          break
# print(f[::-1])

# a=123
# def fff():
#     global a
#     a=111
#     return a
#     print(a)
# print (fff())
#

# c=input('>>:')
# b=c.split(',')
# a=[1,2,3,4,5,6]
# for i,j in enumerate(b):
#     for k in a:
#         if int(b[i])!=k:
#             a.append(int(b[i]))
#     print(a)

# c=input('>>>:')#随机加入一个数，并排序
# c=c.split(',')
# a=[2,4,6,8,18]
# for i in c:
#     a.append(int(i))
#     a.sort()
#     print(a)

# a=input('>>.:')                       #不排序，最大最后最小第一
# a=a.split(',')
# a=[23,343,4345,45]
# b=a.index(max(a))
# d=a.index(min(a))
# a[b],a[d]=a[d],a[b]
# print(a)


# a=input('>>>:')
# b=int(a)
# for i in b:  #错误取值
# for i in range(1,b):
#     s=0
#     # for j in range(1,b):   #错误，取值必须小于i的取值
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#     if s==i:
#         #print(b)  错误：取得值是什么？因数之和等于他本身
#         print(i)

# def dd(x):             #函数：因数之和等于其本身
#     for i in range(1,x):
#         s=0
#         for j in range(1,i):
#             if i%j==0:
#                 s+=j
#         if s==i:
#             print(i)
# dd(1000)

# # def mm(y):      #全部错
# #     d=[x for x in range(1,y) s=0 for j in range(1,x) if x%j==0 s+=j if s==i]
# #     print(d)
# # mm(1000)

# c=input('>>>:')          #??????????
# b=int(c)
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# f=''
# while True:
#     e=b%16
#     b=b//16
#     f+=a[e]
#     if b==0:
#         break
#     print(a[e])
#     print(b)
# print(f[::-1])


# a=input('请输入：')
# a=a.split(',')
# b=input('>>请输入一个数:')
# c=int(b)
# for i in a:
#     if c!=i:
#         break
# else:
#     a[i]

# a=[2,34,45,34,44,23]             #???????????/
# b=int(input('请输入一个数：'))
# for i,j in enumerate(a):
#     if b==j:
#         e=a.index(j)
#         d=a.index(j)-1
#         a[e],a[d]=a[d],j
#         print(a)

# # a=[23,534,343,454,56]
# a=input('>>>:')
# a=a.split(',')
# b=len(a)
# c=a.index(a[b-1])
# print(c)

# a=input('>>>:')                   #cuo
# a=a.split(',')
# b=len(a)
# for i in range(b):
#     for j in range(i+1,b):
#         if a[i]>a[j]:
#             t=a[i]
#             a[i]=a[j]
#             a[j]=t
#             print(a)

# a=[12,321,324,34,34]
# print(a[0::])
    # for j,h in enumerate(a):
    #     if i==(b-1):
    #         break
    #     if int(a[i])<int(a[j+1]) and i:
    #         a[i],a[j+1] = a[j+1],a[i]
    #         print(a)


#     print(a[i])
#
#     if int(a[i])>int(a[i+1]):
#         a[i],a[i+1]=a[i+1],a[i]
#     if int(a[i])<int(a[i+1]):
#         continue
# print(a)
#         # if int(a[i])==int(b-1):
#         #     break





# s=0
# for i in range(1,101):
#     s+=i
# print(s)

# aa=lambda x=2,y=4:x+y
# ss=lambda x,y=4:x*y
# ff=lambda x,y:x//y
# dd=lambda x=9,y=4:x-y
# print(aa(3,4)+45)

# a=input('::::')#计算器加减乘除
# aa=lambda x,y:x+y
# if '+' in a:
#     a=a.split('+')
#     print(aa(int(a[0]),int(a[2])))
# ss=lambda x,y:x-y
# if '-' in a:
#     a = a.split('-')
#     print(ss(int(a[0]),int(a[2])))
# dd=lambda x,y:x*y
# if '*' in a:
#     a = a.split('*')
#     print(dd(int(a[0]),int(a[2])))
# ff=lambda x,y:x/y
# if '/' in a:
#     a = a.split('/')
#     print(ff(int(a[0]),int(a[2])))




# a=100
# print(hex(a))
# print(oct(a))
# print(bin(a))
# aa,bb=divmod(5,3)
# print(aa,bb)


# a=input('>>>')#因素之和
# b=int(a)
# for i in range(1,b):
#     s=0
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#     if s==i:
#         print(i)

# a=input('>>>:')
# a=a.split(',')
# b=max(a)
# print(b)

# a=['电脑','手机','笔记本','二手手机']
# x=input('q')
# b=int(x)
# c=len(a)
# for b in range(1,c):
#     if x==1:
#         print(a[a.index('电脑')])
#     if x==2:
#         print(a[a.index('手机')])
#     if x==3:
#         print(a[a.index('笔记本')])
#     if x==4:
#         print(a[a.index('二手手机')])

# a=input('>>>:')
# b=a.split(',')
# c=b.copy()
# c.sort()
# d,e=c[-1],c[-2]
# f,g=c.count(d),c.count(e)
# print(d*f,e*g)

# def su(x):
#     a = 0
#     for i in range(2,x):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             a+=i
#         print(a)
# su(100)

# a={'电脑':2000,'计算机':5000,'mp3':30}
# for i,j in enumerate(a):
#     print(i+1,j)
# c=input('请输入商品号:')
# b=int(c)
# print(a[b-1])
# b=0
# for i in range(1,100):
#     if i%2==0:#if i%2!=0:
#         b-=i  #b+=i
#     else:
#         b+=i  #b-=i
# print(b)
# print(a)

#

# a=[2,2,2,323,3,3,3,3]
# for i in a:
#     if i==3:
#         a.remove(i)
#         print(a)
#
# x=input(':::')
# b=x.split(',')
# for i in b:
#     if b.count(i)>1:
#         for j in range(b.count(i)-1):
#             b.remove(i)
# print(b)

# a=input('请输入一组数：')           #向左挪一位，未完成
# # a=a.split(',')
# # for i,j in enumerate(a):
# #     a[i]=int(j)
# # b=a.copy()
# # m=max(b)
# # for k in b:
# #     if k==m:
# #         print(k)
# # b.remove(m)
# # m1=max(b)
# # for i in b:
# #     if i==m1:
# #         print(i)


# a=input('>>>:')                                                       # 未完成
# a=a.split(',')
# for i,j in enumerate(a):
#     a[i]=int(j)
# f=a.copy()
# s=len(f)
# b=max(f)
# for i in range(s):
#     if f[i]==b:
#         print(f[i])
#         f.remove(f[i])
# m=max(f)
# n=len(f)
# for j in range(n):
#     if f[j]==m:
#         print(f[j])
#

# a='234'
# b='sfd'
# print(a+b)
# random





# a='342','434','45','45332'          #数据类型转换
# b=list(a)
# print(b)
# print(type(b))
# for i,j in enumerate(b):
#     b[i]=int(j)
# print(b)
# print(type(b))
# e=str(b)
# print(e)
# print(type(e))
# s=set(b)
# print(s)
# print(type(s))
# s=set(a)
# print(s)
# print(type(s))







# a=input('>>>:')
# # a=a.split(',')
# # # e=len(a)
# # for i,j in enumerate(a):
# #     a[i]=int(j)
# # print(a)




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
#             for j in range(10):RR
#                 f.write('wewe'+'\n')


# try:
#     # a='ninini'
#     print(a+1)
# # except Exception as v:                                      #=except:
# #     print(v)
# #     print(123)
# except TypeError or NameError as c:
#     print(c)
#     print('hello')
# # else:
# #     print('wanmei')
#
# def jiujiu(x,y):
#         for  i in range(x,y):
#                 for j in range(1,i+1):
#                         print('{}*{}={}'.format(j,i,j*i),end='\t')
# #                 print()
# a=(1,2,3)
# print(len(a))
# from xlutils.copy import copy
# import paramiko
#
# ssh122=paramiko.Transport((''))
class Ji_scrip():
    def jiu_9(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('{}*{}={}'.format(i,j,i*j),end='\t')
            print()
    def prime_number(self,a):
        num=0
        for i in range(2,a):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                num+=i
        print(num)
    def number_one_two(self,*a):
        for i,j in enumerate(a):
            a[i]=int(j)


a=Ji_scrip()
a.prime_number(100)