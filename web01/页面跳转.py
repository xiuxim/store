
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"D:\python自动化1\python\python\自动化测试\自动化测试7\day01\练习的html\练习的html\跳转页面\pop.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("goo").click()
data=driver.window_handles
driver.switch_to.window(data[1])
time.sleep(2)
driver.find_element_by_id("kw").send_keys("狼腾测试员")
driver.find_element_by_xpath("//*[@class='bg s_btn']").click()

time.sleep(2)

driver.quit()