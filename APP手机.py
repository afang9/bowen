from appium import webdriver
import time
import unittest
#启动设施，连接设备
desired_caps={'platformName':'Android',
              # 'platformVersion':'5.0',
              'deviceName':'127.0.0.1:62001',
              'appPackage':'com.netease.cloudmusic',
              'appActivity':'activity.LoadingActivity'}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print('立即体验')
time.sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
time.sleep(2)
print('')
driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
time.sleep(2)
print('立即登录')
driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
time.sleep(2)
print('手机号')
driver.find_element_by_id('com.netease.cloudmusic:id/aih').click()
time.sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/i1').send_keys('lxf37727@163.com')
time.sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('manman0509')
time.sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
time.sleep(2)
#########断言
class Tes_app(unittest.TestCase):
    driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
    time.sleep(2)
    title=driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
    def test_1(self):
        self.assertEqual(self.title,'九天揽月挽红颜')

if __name__=='__main__':
    unittest.main()
# driver.quit()