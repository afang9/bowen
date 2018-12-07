from selenium import webdriver
import time
from time import sleep
dr=webdriver.Firefox()                   #打开浏览器
dr.get('https://www.sogou.com')        #打开网址
sleep(2)
"""#获取网站的标题（title）
# print(dr.title)                 #通常用来做断言
# #获取网站的网址
# print(dr.current_url)           #通常也是做断言
1,#设置浏览器的大小
dr.set_window_size(200,200)         #第一个宽，第二个是高
sleep(5)
2,#设置浏览器打开的位置
dr.set_window_position(500,200)         #x轴，y轴
sleep(3)
1,2,保证所有的测试用例在所有的测试用例在同一环境下测试
# dr.maximize_window()#浏览器最大化
dr.minimize_window()#浏览器最小化
浏览器的前进后退
dr.get('https://www.sogou.com')
sleep(3)
dr.back()
sleep(2)
dr.forward()        #前进
sleep(1)
# id
# name
# class name
# link text
# partial link text
# tag name
# xpath
# css selecto               ————>1).通过ID来定位
                                        webdriver 模拟人物行为
                                                    --<div(标签)
                                                    --<p(标签)
                                                    --<input(标签)key='values'(标签的属性)
                                                    标签与结束标签中间的是标签的文本(超文本)
                                                    
dr.find_element_by_id('kw').send_keys('清新魏无羡图')                     #通过ID属性定位,定位到ID=kw的位置
sleep(2)
dr.find_element_by_id('su').click()                 #点击
dr.find_element_by_class_name('s_ipt').send_keys('魏无羡')
sleep(2)
dr.find_element_by_class_name('bg s_btn').click()
dr.find_element_by_name('tj_trnews').click()"""
dr.find_element_by_id('zhihu').click()
dr.find_element_by_class_name('query').send_keys('刘亦菲')
dr.find_element_by_class_name('swz').click()
dr.find_element_by_id('zhihu_title_answer_5').click()
# sleep(5)
# dr.quit()                                #关闭浏览器
