# coding:utf-8


from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



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
            # self.mylog.error(u'输入失败,loc='+str(loc)+u';value='+value)

        #   重写find_element方法，增加定位元素的健壮性

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e
            # self.mylog.error(u'找不到元素:'+str(loc))