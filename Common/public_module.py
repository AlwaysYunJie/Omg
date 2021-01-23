# coding:utf-8
import time

from selenium import webdriver

from Omg.Page import login_page


class public_module():

    def login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://omgtest.sumwhy.com/login")
        self.login = login_page.Login_Page(self.driver)
        self.login.input_username("yunjie")
        self.login.input_password("123456")
        time.sleep(10)
        self.login.click_login_button()
        time.sleep(5)
        return self.driver