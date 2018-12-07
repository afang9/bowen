#/usr/bin/env python
#--*-- coding:utf-8 -*-
import random
# def jiujiu():                                     #九九乘法表
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#             print()

# def jiujiu9():                            #while九九乘法表
#     i=1
#     while i<10:
#         j = 1
#         while j<=i:
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#             j+=1
#         print()
#         i+=1
# jiujiu9()


# def zhishu():                                     #质数之和
#     a=0
#     for i in range(2,101):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             a+=i
#     return a
# print(zhishu())

# a=0
# i=2
# while i<101:
#     j=2
#     while j<i:
#         if i%j==0:
#             break
#         j+=1
#     else:
#         a+=i
#     i+=1
# print(a)

# a=input('>>>请输入三个数：')                     #三角形判断
# a=a.split(',')
# a.sort()
# q=int(a[0])
# w=int(a[-1])
# e=int(a[1])
# if q+e>w:
#     print('三角形')
#     if q**2+e**2==w**2:
#         print('直角三角形')
#     elif q**2+e**2>w**2:
#         print('锐角三角形')
#     elif q**2+e**2<w**2:
#         print('钝角三角形')
# else:
#     print('不是三角形')

# def jiecheng(c):                          #阶乘之和
# e=input('请输入一个数：')
# c=int(e)
#     s=1
#     a=0
#     for i in range(1,c+1):
#         s*=i
#         a+=s
#     return a
# print(jiecheng(5))

# def quchong():                        #去重并排序
#     a=input('>>>:')
#     a=a.split(',')
#     b=a.copy()
#     for i in b:
#         if b.count(i)>1:
#             for j in range(b.count(i)-1):
#                 b.remove(i)
#     for k in range(len(b)):
#         b[k]=int(b[k])
#     b.sort()
#     return b
# print(quchong())

# a=input('>>>:')
# a=a.split(',')
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# for k in range(len(b)):
#     b[k]=int(b[k])
# b.sort()
# print(b)


# def huiwen(a):                                #回文
# #     b=a[::-1]
# #     if a==b:
# #         print('huiwen')
# #     else:
# #         print('bushihuiwen')
# # huiwen('werrewr')

# a='qweewq'                                   #回文
# b=len(a)//2
# for i in range(b):
#     if a[i]!=a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')

# a=input('>>>:')                                 # 打印第一大和第二大的
# a=a.split(',')
# for i,j in enumerate(a):
#     a[i]=int(j)
# f=a.copy()
# # s=len(f)
# b=max(f)
# for i in f:
#     if i==b:
#         print(i)
#         f.remove(b)
# # f.remove(b)                           c错
# m=max(f)
# n=len(f)
# for j in range(n):
#     if f[j]==m:
#         print(f[j])

                                                           #删除留一个案列
# f=[3,3,3,2,2]
# b=max(f)
# c=min(f)
# for i in f:
#     if i==b:
#         f.remove(b)
#     elif i==c:
#         f.remove(c)
# # f.remove(b)
# print(f)

#
# a=input('>>>":')
# d=a.split(',')
# c=d.copy()
# c.sort()
# e,f=int(c[-1]),int(c[-2])
# f,g=c.count(e),c.count(f)
# print(f,g)

# a=input('>>>:')                                   #质数之和
# b=int(a)
# for i  in  range(1,b):
#     s=0
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#         if s==i:
#             print(i)

# a='1223243435'                                #不用int将什么变为整数
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for k in range(10):
#         if str(k)==j:
#             s+=k*10**i
#             break
# print(s[::-1])

# e=random.randrange(10)                                    #三次猜数字
# for i in range(3):
#     print('还有{}次机会'.format(3 - i))
#     a = input('请输入一个数')
#     b = int(a)
#     if i>e:
#         print('dale')
#     elif i<e:
#         print('xiaole')
#     elif i==e:
#         print('ganggangde')
#     else:
#         print('cai')

# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']       #十进制转化为十六进制
# b=int(input('请输入数'))
# f=''
# while True:
#      c=b%16
#      b=b//16
#      f=f+a[c]
#      if b==0:
#          break
# print(f[::-1])

# c=input('>>>:')                   #随机加入一个数，并排序
# c=c.split(',')
# a=[2,4,6,8,18]
# for i in c:
#     a.append(int(i))
#     a.sort()
#     print(a)


# c=input('>')             #任意四个数组成三个数
# d=c.split(',')
# a=[]
# for i in d:
#     for j in d:
#         for k in d:
#            if (i!=j) and (j!=k) and (i!=k):
#        #           print(i,j,k)
#                a.append(int(i)*100+int(j)*10+int(k))
# print(a)



# a= input(">>输入年月日>>")
# b= time.strptime("{}".format(a),'%Y %m %d')
# if (b[0]%4 == 0 and b%100 != 0) or b%400 == 0:
#     print('{}是闰年,今天是星期{}，是一年中的第{}天'.format(b[0],b[6]+1,b[7]))
# else:
#     time.sleep(2)
#     print('{}是平年,今天是星期{}，是一年中的第{}天'.format(b[0],b[6]+1,b[7]))