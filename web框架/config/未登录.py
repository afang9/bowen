from selenium import webdriver
from time import sleep
def login_not():
    op=webdriver.Firefox()
    op.get('http://www.moore.ren/')
    # sleep(2)
    return op
# login_not()

