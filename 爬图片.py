import re
import  requests
#反爬：阻止爬虫批量下载资源
#常见的反爬手段：1.通过header信息(headers--User-Agent)2.验证码3.ip被封（西刺代理ping不能有人用的的ip）

# url1='http://www.doutula.com/article/list/?page=1'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# response=requests.get(url=url1,headers=head)
# html=response.content.decode('UTF-8')
# print(html)
# patt=re.compile(r'http://www.doutula.com/article/detail/[0-9]]{7}')
# items=patt.findall(html)
# for i in items:
#     respons=requests.get(url=i,headers=head)
#     html1=respons.content.decode('UTF-8')
#     print(html1)
#     patt1=re.compile(r'<img src="https://ws(.*?) alt')
#     items1=patt1.findall(html1)
#     print(len(items1))
#
#     for j,i in enumerate(items1):
#         i=i.replace("",'')
#         i='http://ws'+1
#             #保存图片
#         tupian=requests.get(i)
#         resl=tupian.content
#         with open('{}.jpg'.format(j),'wb') as f:
#             f.write(resl)

# class Baisi():
#     def qingqiu(self,pic):
#         url='http://www.budejie.com/pic/{}'.format(pic)
#         response=requests.get(url=url)
#         html=response.content.decode('UTF-8')
#         return html
#     def guolv(self,abc):
#         tupian=[]
#         patt=re.compile(r'img src="http://(.*?) title')
#         item=patt.findall(abc)
#         print(item)
    #     for i in item:
    #         print(i)
    #         tupian.append(i)
    #     return tupian
    # def save(self,tupian):
    #     for i,j in enumerate(tupian):
    #         # j = 'http://' + 1
    #         tupian = requests.get(j)
    #         resl = tupian.content
    #         with open('{}.jpg'.format(i),'wb') as f:
    #             f.write(resl)
# baishi=Baisi()
# baishi.qingqiu(1)
# jieguo=baishi.qingqiu(1)
# baishi.guolv(jieguo)
# tupian=baishi.guolv(jieguo)
# baishi.save(tupian)


# import requests
# import re
# class Baisi():
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#     def qingqiu(self):
#         url123='http://www.budejie.com/pic/1'
#         response = requests.get(url=url123,headers=head)
#         html=response.content.decode('UTF-8')
#         return html
#     def guolv(self,html):
#         patt = re.compile(r'"http://mpic.spriteapp.cn(.*?)1.jpg')
#         items = patt.findall(html)
#         return items
#     def save(self,items):
#         for j,i in enumerate(items):
#             # i = i.replace('"','')
#             i = 'https://mpic.spriteapp.cn' + i + '1.jpg'
#             print(i)
#         #保存图片
#             tupian = requests.get(i,verify=False)
#             res1 = tupian.content
#             with open('{}.jpg'.format(j),'wb') as f:
#                 f.write(res1)
# baisi = Baisi()
# aaa = baisi.qingqiu()
# bbb = baisi.guolv(aaa)
# baisi.save(bbb)


