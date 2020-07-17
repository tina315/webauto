'''
websearch
'''

#import webdriver and time
from selenium import webdriver
import time

#start chrome and set windowsize max
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open baidu
driver.get("http://www.baidu.com")
time.sleep(2)

#find text,submit by id and send keys,then click
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

#refresh page
driver.refresh()
time.sleep(2)

#back to last page
driver.back()
time.sleep(2)

#find text by name and send keys,find submit by class name then click
driver.find_element_by_name("wd").send_keys("python")
driver.find_element_by_class_name("s_btn").click()
time.sleep(3)

#find element by link text and click
driver.find_element_by_link_text("Python(计算机程序设计语言)_百度百科").click()
time.sleep(2)
#这时虽打开了新窗口，但webdriver仍然在旧窗口中

#切换窗口
handles = driver.window_handles
driver.switch_to.window(handles[1])

#回到百度首页重新搜索Java
driver.find_element_by_link_text("百度首页").click()
driver.find_element_by_name("wd").send_keys("Java")
driver.find_element_by_class_name("s_btn").click()
time.sleep(3)

#find element by partial link text and click
driver.find_element_by_partial_link_text("百度百科").click()
time.sleep(2)

#close chrome and then quit webdriver
driver.close()
driver.quit()