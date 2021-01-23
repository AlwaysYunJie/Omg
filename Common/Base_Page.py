# coding:utf-8
from selenium.webdriver.android import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
# from api import ShowapiRequest
from Omg.Page import login_page


class BasePage(object):
    def __init__(self,selenium_driver):
        self.driver = selenium_driver

    #   重写send_keys方法
    def send_keys(self, value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as a:
            raise a


        #   重写find_element方法，增加定位元素的健壮性

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e


    def select_value(self, select_way, select_value, *loc):
        try:
            s = self.find_element(*loc)
            print(s.get_attribute("value"))
            print(loc)
            if select_way == 'By_index':
                Select(s).select_by_index(int(select_value))
            elif select_way == 'By_value':
                Select(s).select_by_value(select_value)
            elif select_way == 'By_text':
                Select(s).select_by_visible_text(select_value)
            s.click()
        except Exception as e:
            raise e

