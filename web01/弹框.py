
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get(r"D:\python自动化1\python\python\自动化测试\自动化测试7\day01\练习的html\练习的html\弹框的验证\dialogs.html")
driver.maximize_window()
driver.find_element_by_id("alert").click()
time.sleep(2)

#关闭弹窗
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_id("confirm").click()
time.sleep(2)
# driver.switch_to.alert.accept()

# 模拟键盘（回车，右键）
ac=ActionChains(driver)
ac.send_keys(Keys.END)
ac.send_keys(Keys.ENTER)


time.sleep(2)
driver.quit()