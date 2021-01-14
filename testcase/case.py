# coding:utf-8


import unittest
from time import sleep
from selenium import webdriver
from Page.page import Login_Page
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    def test_baidu_search_case(self):
        page = Login_Page(self.driver)
        page.open()
        page.login_username()
        page.login_password()
        #输入验证码
        sleep(10)
        page.login_clike()
        self.assertEqual(page.get_title(),"selenium_百度搜索")
    @classmethod
    def tearDownClass(cls):
        sleep(10)
        # cls.driver.quit()


