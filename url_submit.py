# encoding=utf-8
"""自动提交url给百度平台
将要提交的url一行一行的放在文本上"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

time.sleep(2)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()

time.sleep(2)
# 百度登录
driver.find_element_by_class_name("tang-pass-footerBar").find_element_by_css_selector(
    "#TANGRAM__PSP_10__footerULoginBtn").click()
# 输入用户名
time.sleep(2)
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("xxxx")
# 输入密码
time.sleep(2)
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("xxxx")

time.sleep(2)
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

time.sleep(2)
driver.get("https://ziyuan.baidu.com/linksubmit/url")

time.sleep(2)
f = open('./url.txt', 'r')
for url in f:
    driver.find_element_by_id("url").send_keys(url)
    driver.find_element_by_id("saveBtn").click()
    time.sleep(3)
    driver.find_element_by_class_name("btn-big-blue").click()
    time.sleep(3)

driver.quit()
