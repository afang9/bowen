from appium import webdriver
from time import sleep
class Login():
    def login_信息(self,zhanghao,password):
        message_music={'platformName':'Android',
                       'deviceName':'127.0.0.1,62001',
                       'appPackage':'com.netease.cloudmusic',
                       'appActivity':'activity.LoadingActivity'}
        driver=webdriver.Remote('http://localhost:4723/wd/hub',message_music)
        driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('{}'.format(zhanghao))
        sleep(2)
        # driver.find_element_by_id('android.widget.RelativeLayout').click()
        # sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('{}'.format(password))
        sleep(2)
        try:
            driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
            sleep(2)
        finally:
            driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
            sleep(2)
        # title = driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
        # print(title)
        return driver
# a=Login()
# a.login_信息()
