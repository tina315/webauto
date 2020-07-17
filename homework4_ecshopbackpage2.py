'''
case:searching practice in ecshop back page(search user)
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open ecshop front page
driver.get("http://localhost/upload/admin/privilege.php?act=login")
time.sleep(2)

#login
driver.find_element_by_name('username').send_keys("admin")
driver.find_element_by_name('password').send_keys("wd19960315")
driver.find_element_by_class_name('button').click()
time.sleep(3)

#get in user list
driver.switch_to.frame('menu-frame')
# #//*[@id="menu-ul"]/li[7]
# #//*[@id="menu-ul"]/li[7]/ul/li[1]/a
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]/ul/li[1]/a').click()


#search user
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
ele = driver.find_element(By.NAME,'user_rank')
select = Select(ele)
select.select_by_visible_text('所有等级')
driver.find_element_by_name('keyword').send_keys('wang')
driver.find_element(By.CSS_SELECTOR,'input[name="keyword"]+input').click()
time.sleep(3)

#close and quit
time.sleep(2)
driver.quit()