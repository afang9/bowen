import selenium.webdriver.support.ui as ui
from web框架.config.未登录 import login_not
from web框架.data.read_Shuju import Click_login
import unittest
from selenium.webdriver.common.action_chains import ActionChains

Click_login().click_login()
class Tes_login_not(unittest.TestCase):
        def test_1(self):
                self.assertEqual(len(self.w),2)
                self.assertNotEqual(self.title_1,self.title_2)


# if __name__=='__main__':
#     unittest.main()
# test_1()


