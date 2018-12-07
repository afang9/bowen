
# op.find_element_by_id('kw').send_keys('摩尔精英')
# sleep(1)
# op.find_element_by_id('su').click()
# op.find_element_by_class_name('OP_LOG_LINK c-text c-text-public c-text-mult c-gap-icon-left').click()
# sleep(2)
# op.quit()
# from selenium import webdriver
# from time import sleep
# op=webdriver.Firefox()
# op.get('http://www.moore.ren')
#link_text#通过文本来定位
# op.find_element_by_link_text('企业').click()
# sleep(2)
# op.find_element_by_link_text('登录').click()
# sleep(2)
# op.find_element_by_link_text('查看更多职位').click()唯一性
# sleep(2)
# op.find_element_by_partial_link_text('登')              #通过模糊文本来定位（元素唯一性）
# sleep(2)
# op.find_element_by_tag_name('').click()             #通过标签的名称去定位，通常用于多个元素的定位
"""op.find_element_by_xpath()                      #通过xpath路径定位方式          xpath路径标记语言
                                                #                   1，绝对路径（/）2,相对路径(//)
                                                xml:可扩展标记语言——>1,xml跟html内容一样
                                                                      2，xml作用:传输和存储数据
                                                                      html主要是显示数据
                                                    xpath主要是在xml里获取资源"""
# op.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[2]/div[1]/div[1]/a').click()
# sleep(2)
# op.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
# # sleep(2)
# op.find_element_by_xpath('//*[@id="search-submit"]').click()
# op.find_element_by_css_selector('body > div.main > div > div.sidebar > div > div:nth-child(4) > div.menu-main > div > h2').click()
# sleep(2)
# op.find_element_by_css_selector('body > div.main > div > div > div.content-left > ul > li:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3 > a').click()
# op.find_element_by_css_selector('body > div.main > div > div > div.content-left > div.pages > a:nth-child(3)').click()
# op.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/a[5]').click()
# op.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[11]/div[2]/div[2]/a').click()
# sleep(2)






# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# op=webdriver.Firefox()
# op.get('http://www.moore.ren')
# w=op.find_elements_by_class_name('menu-box')  #定位多个class属性的值为menmu-box元素    数据类型是列表
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(2)
# op.get('https://www.jd.com/')
# w=op.find_elements_by_class_name('cate_menu_item')
# # 层级定位
# w=op.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')

# w=op.find_element_by_css_selector('#J_cate > ul').find_elements_by_tag_name('li')
# print(len(w))
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(2)
# w=op.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
# print(w.get_attribute('text'))               #获取元素的某个属性的值
# w=op.find_elements_by_xpath('/html/body/div[2]/div/div[2]/dl/dt').text
# print(w)
# print(w.get_attribute('text'))





"""from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
op=webdriver.Firefox()
op.get('http://192.168.0.254/')
sleep(2)
op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
sleep(2)
op.find_element_by_class_name('login_input').send_keys('administrator')
sleep(2)
op.find_element_by_name('txt_password').send_keys('Bane@7766')
sleep(2)
w=op.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_class_name('nobody')
print(len(w))
c=[]
for i in w:
    c.append(i.get_attribute('src')[-5])
for j in c:
    op.find_element_by_class_name('login_yzm').send_keys(j)

# print(w.get_attribute('src'))
sleep(2)
op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
sleep(2)"""



"""from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
op=webdriver.Firefox()
op.get('http://www.ctrip.com/')
op.find_element_by_class_name('current').click()
sleep(2)
op.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
sleep(2)
w=op.find_element_by_css_selector('#J_roomCountList').find_elements_by_tag_name('option')
print(type(w))
for i in w:
    ActionChains(op).move_to_element(i).perform()
# sleep(2)
# op.find_element_by"""


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# op=webdriver.Chrome()
# op.get('http://www.moore.ren/')
#
# op.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# # sleep(2)
#
# print(op.current_window_handle)   #获取当前窗口的句柄
# print(op.title)
# w=op.window_handles
# print(w)
# op.switch_to.window(w[-1])          #根据句柄切换窗口
# print(op.title)
# q=op.current_window_handle
# w=op.window_handles
# for i in w:
#     if i !=q:
#         op.switch_to_window(i)
# op.find_element_by_xpath('//*[@id="emailInput"]').send_keys('lxf37727@163.com')


# op.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
# q=op.current_window_handle
# w=op.window_handles
# for i in w:
#     if i!=q:
#         op.switch_to.window(i)
# op.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys('17530128905')
# sleep(2)
# op.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('manman0509')



""""# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# op=webdriver.Firefox()
# op.get('https://i.qq.com/')
# sleep(2)
# op.switch_to.frame('login_frame')
# op.find_element_by_css_selector('#switcher_plogin').click()
# # op.switch_to.frame('login_frame')            #切换到内置框架
# # 只能根据：id、name、定位到框架    来切换
# # w=op.find_element_by_xpath('//*[@id="login_frame"]')
# # op.switch_to.frame(w)
# op.find_element_by_xpath('//*[@id="u"]').send_keys('1241378256')
# sleep(2)
# op.find_element_by_xpath('//*[@id="p"]').send_keys('MANMAN0509')
# sleep(2)
# op.find_element_by_xpath('//*[@id="login_button"]').click()
# op.switch_to.default_content()          #退出到原始界面
# op.switch_to.parent_frame()
# op.quit()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
op=webdriver.Chrome()
# op.get('http://www.moore.ren/')
# w=op.find_elements_by_class_name('menu-box')
# print(len(w))
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(2)
# op.get('https://www.jd.com/')
# # op.find_element_by_class_name('cate_menu_item')
# w=op.find_element_by_css_selector('#J_cate > ul').find_elements_by_tag_name('li')
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(2)

# op.get('https://www.taobao.com/')
# w=op.find_elements_by_class_name('J_Cat a-all')
# # w=op.find_element_by_css_selector('body > div.screen-outer.clearfix > div.main > div.main-inner.clearfix > div.tbh-service.J_Module > div > ul').find_elements_by_tag_name('li')
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(1)
# op.quit()

# op.get('https://www.jd.com/')
# # w=op.find_elements_by_class_name('cate_menu_item')
# # for i in w:
# #     ActionChains(op).move_to_element(i).perform()
# #     sleep(2)
# w=op.find_element_by_xpath('//*[@id="J_cate"]').find_elements_by_tag_name('li')
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(2)

# op.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
# op.switch_to.frame('')
# w=op.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[5]')
# op.switch_to.frame(w)
# op.find_element_by_partial_link_text('账户登录').click()
# op.find_element_by_css_selector('#loginname').send_keys('17530128905')
# op.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('manman0509')
# op.find_element_by_css_selector('#loginsubmit').click()
# sleep(2)"""


"""op.get('http://192.168.0.254')
sleep(2)
op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
op.find_element_by_css_selector('#userLoginBox > form > ul > li:nth-child(2) > input').send_keys('Bane@7766')
w=op.find_elements_by_class_name('nobody')
print(w)
c=[]
for i in w:
    c.append(i.get_attribute('src')[-5])
for j in c:
    op.find_element_by_xpath('//*[@id="input1"]').send_keys(j)
    sleep(1)

op.find_element_by_css_selector('#userLoginBox > form > ul > li.fixline.btn > input.login_btn2').click()
w=op.switch_to_alert()          #切换到弹出框
sleep(2)
print(w.text)           #获取弹出框的文本
sleep(1)
w.accept()              #点击确定"""



# op.get('https://www.jd.com/')
# w=op.find_element_by_xpath('//*[@id="J_cate"]').find_elements_by_tag_name('li')
# print(len(w))
# for i in w :
#     print(i.get_attribute('class'))
#     sleep(1)

"""op.get('http://192.168.0.254')

op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
#弹出框 alert
w=op.switch_to_alert()          #切换到弹出框
sleep(2)
print(w.text)           #获取弹出框的文本
sleep(1)
w.accept()              #点击确定
w.dismiss()         #点击取消
w.send_keys('')         #输入弹出框要求的内容"""
# op.get('http://www.alltuu.com/login?url=http://www.alltuu.com/v')
# op.find_element_by_css_selector('#loginUsername').send_keys('17530128905')
# w=op.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# print(len(w))
# for i in w:
#     ActionChains(op).move_to_element(i).perform()
#     sleep(1)
#     if '.com' not in i.text:
#         i.click()
#
# op.find_element_by_class_name('form-control').send_keys('manman0509')
# op.find_element_by_partial_link_text('登').click()
# op.find_element_by_partial_link_text('@163.com').click()
# z=op.find_element_by_xpath('/html/body/ul').text()
# print(z)




import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
op=webdriver.Chrome()


# op.get('http://192.168.0.254')
# sleep(2)
# op.find_element_by_class_name('login_input').clear()
# op.find_element_by_name('txt_name').send_keys('administrator')
# op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# w=op.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_tag_name('img')
# c=[]
# for i in w:
#     c.append(i.get_attribute('src')[-5])
# for j in c:
#     op.find_element_by_class_name('login_yzm').send_keys(j)
#     sleep(1)
# op.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(2)
# d=op.switch_to_alert()
# print(d.text)
# d.accept()
# w=op.find_element_by_xpath('//*[@id="Content"]/frame[1]')
# op.switch_to_frame(w)
# op.find_element_by_xpath('//*[@id="04"]/span[2]').click()
# sleep(1)
# op.find_element_by_xpath('//*[@id="041"]/span').click()
# # op.switch_to_frame('main')
# a=op.find_element_by_xpath('//*[@id="main"]')
# op.switch_to_frame(a)
# b=op.find_element_by_xpath('//*[@id="Content"]/frameset')
# op.switch_to_frame(b)
# op.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# q=op.find_element_by_xpath('//*[@id="mainnav_body"]/table/tbody/tr/td').find_elements_by_tag_name('div')
# sleep(2)


# for i in q:
# #     if i not in a:
# #         a.append(i)
# # for j in a :
#     ActionChains(op).move_to_element(i).perform()
#     sleep(1)
#     print(i.text)
#     if i.text == "防火墙":
#         i.click()
#         break

# op.quit()

# op.get('http://qzone.qq.com/')
"""移动滚动条       属于浏览器的   属于JavaScript语言在浏览器加入的功能
var q=document.documentElement.scrollTop=10000
                1,根据页面的高度来移动滚动条
                        控制滚动条的JavaScript代码
                        10000表示所有网页的高度
                            数字越大、滚动越往下
                            元素指的是页面上的数据"""
# for i in range(0,8500,500):
#     js="var q=document.documentElement.scrollTop={}".format(i)
#     sleep(1)
#     op.execute_script(js)           #执行JavaScript语句
"""根据定位到的元素来移动滚动条
"""
# w=op.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[6]/div/div[3]')
# js='arguments[0].scrollIntoView();'
# op.execute_script(js,w)
# op.switch_to_frame('login_frame')
# op.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# op.find_element_by_css_selector('#u').send_keys('37727871')
# sleep(1)
# op.find_element_by_xpath('//*[@id="p"]').send_keys('qwewre')
# sleep(1)
# op.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# f=op.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# op.switch_to_frame(f)
# start=op.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# ActionChains(op).drag_and_drop_by_offset(start,181,0).perform()



"""
强制等待        sleep()
智能等待--设置控制器op等待
is_displayed判断元素有木有显示在屏幕上       结果:True   Flase
is_enabled判断元素是否为灰化状态"""
# op.get('http://www.moore.ren/')
# op.maximize_window()
# sleep(2)
# until=ui.WebDriverWait(op,10)
# until.until(lambda op:op.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())
# # w=op.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_enabled()
# w=op.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed()
# print(w)
# # sleep(2)
# op.get_screenshot_as_png()
# op.save_screenshot('保存截图名字.png')
# # op.get_screenshot_as_file('截图保存的文件名')

op.quit()