from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HTMLTestRunnertest
op=webdriver.Firefox()
op.get('https://www.jd.com/')
op.find_element_by_xpath('')