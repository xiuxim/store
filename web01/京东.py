
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='key']").send_keys("手机")
driver.find_element_by_xpath("//*[@class='button']").click()
time.sleep(2)

data=driver.window_handles
driver.switch_to.window(data[0])

driver.find_element_by_xpath("//div[@class='gl-i-wrap']").click()
time.sleep(5)
data=driver.window_handles
driver.switch_to.window(data[1])

# driver.find_element_by_link_text("加入购物车").click()
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(5)
driver.switch_to.frame("dialogIframe")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("15111111111")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("15111111111")
driver.find_element_by_xpath("//*[@class='btn-img btn-entry']").click()
time.sleep(3)
ac=ActionChains(driver)
a=driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
ac.click_and_hold(a).move_to_offset(108,0).perform()
