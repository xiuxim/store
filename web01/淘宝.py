
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.taobao.com/")
driver.maximize_window()
driver.find_element_by_id("q").send_keys("手机")
driver.find_element_by_xpath("//button[@class='btn-search tb-bg']").click()
# 窗口切换
data=driver.window_handles
driver.switch_to.window(data[0])

driver.find_element_by_id("fm-login-id").send_keys("151*******")
driver.find_element_by_id("fm-login-password").send_keys("**********")
time.sleep(5)

ac=ActionChains(driver)
a=driver.find_element_by_xpath("//span[@class='nc-lang-cnt']")

ac.click_and_hold(a).move_by_offset(300,0).perform()
time.sleep(5)
driver.find_element_by_link_text("登录").click()

