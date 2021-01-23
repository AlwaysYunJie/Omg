# coding:utf-8


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Omg.Page import sell_page
from Omg.Page import login_page
import unittest,time
from Omg.Common.Base_Page import BasePage
from Omg.Common import public_module

S = BasePage.login()
class Test_xinasuo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module
        cls.driver = cls.PM.login()
        cls.PM.login()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get("http://omgtest.sumwhy.com/login")
    #     self.login = login_page.Login_Page(cls.driver)
    #     self.login.input_username("yunjie")
    #     self.login.input_password("123456")
    #     time.sleep(10)
    #     self.login.click_login_button()
    #     time.sleep(5)
    #
    # def tearDown(self):
    #     self.driver.close()

    """
    进入线索，输入公司名称，是否成功查询到指定公司
    """
    def test_xiansuo_001(self):
        self.xiansuo = sell_page.Sell_Page(self.driver)
        self.xiansuo.click_menu()
        time.sleep(2)
        self.xiansuo.click_xiansuo()
        time.sleep(2)
        self.xiansuo.input_company_name("青青子衿")
        time.sleep(2)
        self.xiansuo.click_search()
        time.sleep(1)
        self.assertIn(u'青青子衿',self.xiansuo.get_xiansuo_name())

    """
    搜索重要状态为高的公司
    """
    def test_xiansuo_002(self):
        self.xiansuo = sell_page.Sell_Page(self.driver)
        self.xiansuo.click_menu()
        time.sleep(2)
        self.xiansuo.click_xiansuo()
        time.sleep(2)
        self.xiansuo.click_importance()
        time.sleep(1)
        # self.xiansuo.importance_status(u'高')
        self.xiansuo.click_importance_status()
        self.xiansuo.click_search()
        self.assertIn(u'高', self.xiansuo.get_importance_list())

    """
    搜索线索为全部的线索
    """
    def test_xiansuo_003(self):
        self.xiansuo = sell_page.Sell_Page(self.driver)
        self.xiansuo.click_menu()
        time.sleep(2)
        self.xiansuo.click_xiansuo()
        time.sleep(2)
        self.xiansuo.click_Allocation()
        time.sleep(1)
        self.xiansuo.click_Allocation_status()
        self.xiansuo.click_search()
        self.assertIn(u'否', self.xiansuo.get_allpcation())

    """
    搜索状态为已分配的状态
    """
    def test_xiansuo_004(self):
        self.xiansuo = sell_page.Sell_Page(self.driver)
        self.xiansuo.click_menu()
        time.sleep(2)
        self.xiansuo.click_xiansuo()
        time.sleep(2)
        self.xiansuo.click_distribution()
        time.sleep(2)
        self.xiansuo.click_distribution_status()
        time.sleep(2)
        self.xiansuo.click_search()
        self.assertIn(u'已分配', self.xiansuo.get_distribution())