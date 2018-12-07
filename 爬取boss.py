import requests
import re

url='https://www.zhipin.com/c101020100/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&ka=sel-salary-0'
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
response=requests.get(url=url,headers=head)
html=response.content.decode('utf-8')
print(html)
# shuju=[]
patt=re.compile('<div class="job-title">(.*?)</div>',re.S)
items=patt.findall(html[0])
print(items)
