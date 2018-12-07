from APP框架.config.Music_定域 import Login
from APP框架.data.Music_提取 import read_shuju
import unittest
import HTMLTestRunnertest
from appium import webdriver
from time import sleep
class Tes_conditions(unittest.TestCase):
    shuju = read_shuju()
    def test_login(self):
        driver=Login().login_信息(self.shuju[1][0],self.shuju[1][1])
        # driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        # sleep(2)
        title = driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
        self.assertEqual(title, '九天揽月挽红颜')
    def test_not_login_1(self):
        driver=Login().login_信息(int(self.shuju[0][0]),self.shuju[0][1])
        # driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        # sleep(2)
        title=driver.find_element_by_id('com.netease.cloudmusic:id/pt').text
        sleep(2)
        self.assertEqual(title,'登录')
        print('失败')
    def test_not_login_2(self):
        driver=Login().login_信息(int(self.shuju[2][0]),self.shuju[2][1])
        # driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        # sleep(2)
        title=driver.find_element_by_id('com.netease.cloudmusic:id/pt').text
        sleep(1)
        self.assertTrue(title,'登录')
        print('失败')
if __name__=='__main__':
    unittest.main()
