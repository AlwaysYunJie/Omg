# coding:utf-8

from Omg.Common.Base_Page import BasePage
from selenium.webdriver.common.by import By

class   Edit_Sell_Page(BasePage):

    # 定位器

    # 公司名称超链接
    bluelinks = (By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div/button/span")

    def click_bluelinks(self):
        self.find_element(*self.bluelinks).click()