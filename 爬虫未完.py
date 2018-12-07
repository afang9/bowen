import requests
import re
#面向对象代码
#第一部分析网址的代码

# class Qiushi(object):
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #发送请求de 代码
#         response=requests.get(url=url)
#         #读取结果的方式 1.以字符串的方式读取2.以字节码的方式读取(需要解码,编码方式需要查看网络源的编码方式)
#         # print(response.text)
#         # print(response.content.decode('utf-8'))
#         html=response.content.decode('utf-8')
#         return html
#         #爬虫第二部：分析html文件，过滤并下载想要的资源文件
#     def guolv(self,abc):
#         shuju=[]
#         patt=re.compile('<div class="content">(.*?)</div>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','').replace('</span>','').replace('<br/>','').replace('<span class="contentForAll">查看全文','').strip()
#             print(i)
#             shuju.append(i)
#         return shuju
#         #爬虫的第三步：保存，保存的权限和格式
#     def save(self,shuju):
#         with open('as.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')
# for j in range(1,6):
#     qiushi=Qiushi()
#     qiushi.qingqiu(j)
#     jieguo=qiushi.qingqiu(j)
#     qiushi.guolv(jieguo)
#     shuju=qiushi.guolv(jieguo)
#     qiushi.save(shuju)


# import requests
# class Qiushi(object):
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         response=requests.get(url=url)
#         html=response.text
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         patt=re.compile('<div class="content">(.*?)</div>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','').replace('</span>','').replace('<br/>','').replace('<span class="contentForAll">查看全文','').strip()
#             print(i)
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('ac.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')
# qiushi=Qiushi()
# qiushi.qingqiu(1)
# jieguo=qiushi.qingqiu(1)
# qiushi.guolv(jieguo)
# shuju=qiushi.guolv(jieguo)
# qiushi.save(shuju)

#
# import re
# import requests
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import os
# class Douban():
#     def qingqiu(self,start):
#         url='https://book.douban.com/top250?start={}'.format(start)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#         response=requests.get(url=url,headers=head)
#         html=response.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         title=[]
#         jianjie2=[]
#         patt=re.compile(r' <td valign="top">(.*?)</td>',re.S)
#         items=patt.findall(html)
#         jianjie=re.compile(r'<span class="inq">(.*?)</span>',re.S)
#         new_items=jianjie.findall(html)
#         for i in items:
#             title1=re.findall(r'title="(.*)"',i,re.S)
#             jianjie1=re.findall(r'<span class="inq">(.*?)</span>',i,re.S)
#             if jianjie1==0:
#
#                 title.append(title1[0])
#                 jianjie2.append(jianjie1[0])
#             if i=='可试读':
#                 items.remove(i)
#         # shuju=zip(items,new_items)
#         return title,jianjie
#         # return shuju
#     def save(self,shuju):
#         if 'bb.xls' not in os.listdir():
#             f=xlwt.Workbook()
#             abc=f.add_sheet('python操作豆瓣')
#             abc.write(0,0,'书名')
#             abc.write(0,1,'简介')
#             for i in range(len(shuju)):
#                 abc.write(i+1,0,shuju[0][i])
#                 abc.write(i+1,1,shuju[1][i])
#             f.save('bb.xls')
#         else:
#             f=xlrd.open_workbook('bb.xls')
#             sheet=f.sheet()[0]
#             hang=sheet.nrows
#             new_f=copy(f)
#             sheet=new_f.get_sheet(0)
#             for i in range(len(shuju)):
#                 sheet.write(i+hang,0,shuju[0][i])
#                 sheet.write(i+hang,1,shuju[1][i])
# douban=Douban()
# for i in range(0,226,25):
#     douban.qingqiu(i)
#     jieguo=douban.qingqiu(i)
#     douban.guolv(jieguo)
#     zhuti=douban.guolv(jieguo)
#     douban.save(zhuti)
#
# import re
# import requests
# class Shengxu():
#     def qingqiu(self):
#         for i in range(50):
#             url='https://www.77nt.com/88849/{}.html'.format(24727754+i)
#             # url='https://www.77nt.com/88849/24727754.html'
#             response=requests.get(url=url)
#             html=response.content.decode('gbk')
#         return html
#
#     def guolv(self,abc):
#         zhangjie=[]
#         patt=re.compile('</script></div>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<div class',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             print(i)
#             zhangjie.append(i)
#         return zhangjie
#     def save(self,zhangjie):
#         with open('aaa.txt','a',encoding='utf-8') as f:
#             for i in zhangjie:
#                 f.write(i+'\n')
# shengxu=Shengxu()
# shengxu.qingqiu()
# jieguo=shengxu.qingqiu()
# shengxu.guolv(jieguo)
# zhangjie=shengxu.guolv(jieguo)
# shengxu.save(zhangjie)
import requests
import re
import os
class Qshi():
    def qingqiu(self,page):
        url='https://www.doutula.com/article/list/?page={}'.format(page)
        # print(url)
        head={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36'}
        response=requests.get(url=url,headers=head)
        html=response.content.decode('utf-8')
        # print(html)
        return html
    def guolv(self,html):
        mu=[]
        # with open('{}.txt'.format(file),'w',encoding='utf-8')as f:
        #     f.write('{}'.format())
        patt=re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        items=patt.findall(html)
        # print(items)
        file=re.compile(r'<div class="random_title">(.*?)<div ',re.S)
        # print(items)
        new_items=file.findall(items[0])
        # print(new_items)
        for i in new_items:
            if i!='赞助商广告</div>\n':
                mu.append(i)
        # print(mu)
        # for j in mu:
        #     os.mkdir(r'C:\Users\旭方\Desktop\log\{}'.format(j))
        patt_5=re.compile('<a href="(.*?)"')
        itmes_5=patt_5.findall(items[0])
        # print(itmes_5)
        for jj in itmes_5:
            url=jj
            head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36'}
            res=requests.get(url=jj,headers=head)
            html_6=res.content.decode('utf-8')
            print(html_6)
            patt_6=re.compile('this.src=(.*?)',re.S)
            items_6=patt_6.findall(html_6[0])
            print(items_6)
            break



qshi=Qshi()
html=qshi.qingqiu(3)
qshi.guolv(html)


