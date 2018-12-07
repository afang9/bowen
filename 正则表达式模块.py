import re
            #导入正则表达式模块          只能匹配（过滤）字符串      附给一个变量
            #贪婪模式：尽可能多的去匹配最后的字符串
            #非贪婪模式：尽可能少的去匹配最后的字符串
            #带有？的是非贪婪，带有*的是贪婪
            #贪婪模式和非贪婪模式的区别：
            #   .匹配任意一个字符，除了换行符，    在编译一行后加入re.S    re.I匹配的字符不区分大小写
# a='qwe123qweqwe323qweqwe321qwe'
# a="""qwe12qwe234qwe
# qwe12qwe456qwe
# qwe23qwe
# qwe678
# qwe"""
#             #首先将要匹配的正则编译
# b=re.compile('qwe(.{})qwe')
# b=re.compile('qwe(.{4}?)qwe')
# b=re.compile('qwe(.*?)qwe',re.S)
# b=re.compile('QWE(.*?)QWE',re.I)
# b=re.compile('qweqwe')
#             #到目的字符串中查找
# c=b.findall(a)
# print(c)