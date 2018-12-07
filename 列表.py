# name_list=['张丹','王武','小张']
"""修改"""
# name_list[2]='言语'
# print(name_list)
"""增加"""
# name_list.append('牛批')
# print(name_list)
# name_list.insert(4,'小明')
# print(name_list)
# temp_list=['孙小圣','猪二哥','沙和尚']
# name_list.extend(temp_list)
# print(name_list)
"""删除"""
"""remove指定删除数据"""
# temp_list.remove('猪二哥')
# print(temp_list)
# temp_list.pop(1)
"""clrear可以清空列表"""
# temp_list.clear()
# print(temp_list)
"""pop不带参数直接删除最后一个索引值"""
# temp_list.pop()
# temp_list=['孙小圣','猪二哥','沙和尚']
"""del删除表中数据的索引"""
# del temp_list[1]
# print(temp_list)
"""del删除变量名不能用print来输出结果"""
# name='小张'
# del name
# # print(name)
# temp_list=['孙小圣','猪二哥','沙和尚','孙小圣']
# name_list=['张丹','王武','小张']
# sum_xuehao=['6','8','2','9','3','1']
"""count统计列表中相同元素的个数"""
# temp_1=temp_list.count('孙小圣')
# # print(temp_1)
# name_list.sort()
# print(name_list)
"""升序"""
# sum_xuehao.sort()
# print(sum_xuehao)
"""降序"""
# sum_xuehao.sort(reverse=True)
# print(sum_xuehao)
"""逆序"""
# sum_xuehao.reverse()
"""['1', '3', '9', '2', '8', '6']"""
# print(sum_xuehao)
import keyword
"""['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""
# print(keyword.kwlist)
a=[1,2]
"""[1, 2, 1, 2]"""
# print(a*2)
a=(1,2)
"""(1, 2, 1, 2, 1, 2)
"""
# print(a*3)
a=[12,23]
b=['we','we']
"""[12, 23, 'we', 'we']"""
s=a+b
# print(s)
a.extend(b)
"""[12, 23, 'we', 'we']"""
# print(a)
c=['rr']
# a.append(c)
"""[12, 23, 'we', 'we', ['rr']]"""
a.append(10)
"""[12, 23, 'we', 'we', 10]"""
# print(a)
"""in  not in 只能针对字典key是否存在"""
# print('bbb' in {'f':'bbb'})
for i in [1,2,3,4]:
    if i==0:
        print(i)
        break

else:
    print('会执行吗？')
