from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r"D:\python自动化1\python\python\自动化测试\自动化测试7\day01\练习的html\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()
driver.find_element_by_id("accountID").send_keys("lxx")
driver.find_element_by_id("passwordID").send_keys("123456")
# 点击下拉框选项
s = driver.find_element_by_id("areaID")
# Select(s).select_by_index(1)
# Select(s).select_by_value("beijing")
Select(s).select_by_visible_text("北京市")
s.click()
# 下拉框
# driver.find_element_by_id("areaID").send_keys("北京市")

driver.find_element_by_id("sexID2").click()
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()
# 上传文件
driver.find_element_by_name("file").send_keys(r'D:\Users\lxx\Desktop\22.txt')

driver.find_element_by_id("buttonID").click()
sleep(2)
# 关闭弹窗
driver.switch_to.alert.accept()
sleep(2)
driver.quit()
