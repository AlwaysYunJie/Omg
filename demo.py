import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()


driver.get("http://omgtest.sumwhy.com/login")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[1]/div/div/input").send_keys("yunjie")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[2]/div/div[1]/input").send_keys(123456)
time.sleep(10)
driver.find_element_by_xpath("//*[text()='登录']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[text()='线索']").click()
time.sleep(3)
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//ul[@class='ivu-select-dropdown-list']/li[contains(text(),'高')]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/input").send_keys("君子")
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/button[1]").click()
time.sleep(10)
driver.quit()
