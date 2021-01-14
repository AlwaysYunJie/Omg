from selenium import webdriver
from Page import login_page
import unittest
import time
class Test_Login(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://omgtest.sumwhy.com/login")

    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_001(self):
        self.login = login_page.Login_Page(self.driver)
        self.login.input_username("yunjie")
        self.login.input_password("123456")
        time.sleep(10)
        self.login.click_login_button()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()