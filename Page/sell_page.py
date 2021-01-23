# coding:utf-8


from Omg.Common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class Sell_Page(BasePage):

    # 定位器
    menu = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/span") #销售中心按钮
    xiansuo = (By.XPATH, "//*[text()='线索']")  #线索按钮
    company_name = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/input") # 公司名输入框
    # 创建日期后续加入
    importance = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div/span")  # 重要性状态
    imp_status = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[contains(text(),'高')]")  # 重要状态高
    Allocation = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div/span") # 线索状态
    allocation_status = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[contains(text(),'有效线索')]")  # 线索状态全部
    distribution_status = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/span") # 分配状态
    bution_status = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[contains(text(),'已分配')]")  #分配状态已分配
    search = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/button[1]") # 查询按钮
    reset = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/button[2]") # 重置按钮
    distribution = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/button[3]") # 分配按钮
    xiansuo_list_loc = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/div/div/button') # 列表公司名第一行
    # xiansuo_list_loc = (By.CLASS_NAME,'ivu-table-column-YfvMhx')
    importance_list_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[5]/div/div/div/span") # 列表重要性第一行
    allocation_list_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[11]") # 列表线索第一行
    distribution_list_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/div/div") # 列表分配状态第一行

    # 点击线索中心
    def click_menu(self,):
        self.find_element(*self.menu).click()

    # 点击线索
    def click_xiansuo(self):
        self.find_element(*self.xiansuo).click()

    # 输入公司名称
    def input_company_name(self,company_name):
        self.send_keys(company_name,*self.company_name)


    # 点击查询
    def click_search(self):
        self.find_element(*self.search).click()

    # 点击重要性按钮
    def click_importance(self):
        self.find_element(*self.importance).click()

    # 重要性下拉
    def importance_status(self,imp_status):
        self.select_value('By_text', imp_status, *self.importance)

    # 选择重要性为高的重要性状态
    def click_importance_status(self):
        self.find_element(*self.imp_status).click()

    # 点击线索按钮
    def click_Allocation(self):
        self.find_element(*self.Allocation).click()

    # 点击线索状态有效
    def click_Allocation_status(self):
        self.find_element(*self.allocation_status).click()

    # 点击分配状态按钮
    def click_distribution_bution(self):
        self.find_element(*self.distribution_status).click()

    # 点击分配状态为已经分配
    def click_distribution_status(self):
        self.find_element(*self.bution_status).click()

    # 点击重置按钮
    def click_resst(self):
        self.find_element(*self.reset).click()

    # 点击分配按钮
    def click_distribution(self):
        self.find_element(*self.distribution_status).click()

    # 列表第一行的公司名称
    def get_xiansuo_name(self):
        return self.find_element(*self.xiansuo_list_loc).text

    # 列表第一行重要性名称
    def get_importance_list(self):
        return self.find_element(*self.importance_list_loc).text

    # 列表第一行线索名称
    def get_allpcation(self):
        return self.find_element(*self.allocation_list_loc).text

    # 列表第一行分配状态名称
    def get_distribution(self):
        return self.find_element(*self.distribution_list_loc).text