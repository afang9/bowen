from web框架.config.未登录 import login_not
class Click_login():
    def click_login(self):
        op=login_not()
        # print(op)
        title_1=op.title
        # print(title_1)
        op.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        print(op.current_window_handle)
        w=op.window_handles
        op.switch_to_window(w[-1])
        title_2=op.title
        aa=list(zip(title_1,title_2,w))
        return aa
# if __name__=='__main__':
#     print(Click_login().click_login())
# a=Click_login()
# print(a.click_login())