'''
searching procedure in baidu
'''

#import webdriver
from selenium import webdriver
import time

#open chrome,max window and sleep
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

#open baidu
driver.get("http://www.baidu.com")
#sleep 1 second
time.sleep(1)
# #find text and input
# driver.find_element_by_id("kw").send_keys("python")
# #sleep 2 seconds
# #time.sleep(2)
# #click buttom
# driver.find_element_by_id("su").click()
# #sleep 5 seconds
# #time.sleep(5)

#find text and input
driver.find_element_by_name("wd").send_keys("python")
#sleep 2 seconds
#time.sleep(2)
#click buttom
# driver.find_element_by_class_name("btn self-btn bg s_btn").click()
#定位页面与操作页面可能不同（由登录导致的，可能访问的服务器并不相同）#
# driver.find_element_by_class_name("bg s_btn").click()
# #元素不唯一也会导致出错,class中多个数据可以单个验证,只用唯一的那个值即可
driver.find_element_by_class_name("s_btn").click()
# sleep 2 seconds
time.sleep(2)
# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">

#click link
# driver.find_element_by_link_text("python教程-【免费】教程").click()
# driver.find_element_by_partial_link_text("python教程").click()
driver.find_element_by_partial_link_text("【免费】教程").click()