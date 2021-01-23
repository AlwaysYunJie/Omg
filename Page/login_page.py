# coding:utf-8


from Omg.Common.Base_Page import BasePage
from selenium.webdriver.common.by import By

class Login_Page(BasePage):
    # url = "http://omgtest.sumwhy.com/login"


    #定位器
    username = (By.XPATH,'/html/body/div[1]/div/div/div[1]/div/form/div[1]/div/div/input')
    password = (By.XPATH,'/html/body/div[1]/div/div/div[1]/div/form/div[2]/div/div[1]/input')
    login_button = (By.XPATH,"//*[text()='登录']")




    def input_username(self,username):
        self.send_keys(username,*self.username)

    # 输入密码
    def input_password(self,password):
        self.send_keys(password,*self.password)

    # 点击登录按钮
    def click_login_button(self):
        self.find_element(*self.login_button).click()

    # def user_icon(self):
    #     return self.find_element(*self.user_icon).is_displayed()
