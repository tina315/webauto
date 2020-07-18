'''
case:searching practice in jd
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open jd
driver.get("http://www.jd.com")
time.sleep(2)

# #get ticekt进入领取优惠券页面
# driver.execute_script("window.scrollTo(100,950)")
# time.sleep(2)
# driver.find_element(By.XPATH,'//div[@id="J_coupon"]/div[2]/div/div/div[1]/a/div[1]').click()
# time.sleep(2)
#回到页面顶部
# driver.execute_script("window.scrollTo(0,0)")
# time.sleep(2)
#到页面底部
# xy = driver.find_element_by_tag_name('html').size
# print(xy)  #打标记
# driver.execute_script("window.scrollTo(0,"+str(xy["height"])+")") #方法1
# # driver.execute_script("window.scrollTo(0,%s)"%(xy["height"]))   #方法2
# time.sleep(2)

#鼠标悬浮在菜单栏上
loc = driver.find_element_by_link_text('家用电器')
action = ActionChains(driver)
action.move_to_element(loc).perform()
time.sleep(2)
#点击冰箱
driver.find_element(By.XPATH,'//div[@id="cate_item1"]/div[1]/div[2]/dl[4]/dt/a').click()
time.sleep(2)
#切换窗口
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
print(driver.title)
#搜索内容
driver.find_element(By.XPATH,'//input[@id="key"]').clear()
time.sleep(1)
driver.find_element(By.ID,'key').send_keys('haier')
time.sleep(1)
driver.find_element_by_id('key').send_keys(Keys.ENTER)
time.sleep(2)

# 在元素上单击鼠标左键
# # action.click_and_hold(loc).perform()
# # time.sleep(2)
# # action.release().perform()
# # time.sleep(2)
#鼠标右键单击
# action.context_click(loc).perform()
# action.release(loc).perform()
# time.sleep(2)
#左键双击
# action.double_click(loc).perform()   #会打开多个重复窗口
# action.release(loc).perform()
# time.sleep(2)
# #鼠标拖拽（无法实现但也不报错）
# loc1 = driver.find_element_by_id('key')
# action.drag_and_drop(loc,loc1)
# action.perform()
# time.sleep(3)

# #悬浮地址栏上
# addr = driver.find_element(By.XPATH,'//a[@id="areamini"]')
# action = ActionChains(driver)
# action.move_to_element(addr).perform()
# time.sleep(3)

#close and quit
time.sleep(2)
driver.quit()