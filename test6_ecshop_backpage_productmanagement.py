'''
case:searching practice in ecshop back page(backpage management)
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

#get in add product
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]/ul/li[2]/a').click()
time.sleep(1)
driver.switch_to.default_content()

#add product
driver.switch_to.frame('main-frame')
driver.find_element_by_name('goods_name').send_keys('辣条')
time.sleep(2)
driver.execute_script("document.getElementById('promote_start_date').removeAttribute('readonly')")
driver.find_element_by_id('promote_start_date').clear()
driver.find_element_by_id('promote_start_date').send_keys('2020-01-01')
time.sleep(3)
driver.execute_script("document.getElementById('promote_1').removeAttribute('disabled')")
driver.find_element_by_id('promote_1').clear()
driver.find_element_by_id('promote_1').send_keys('1.99')
time.sleep(3)
driver.switch_to.default_content()


#close and quit
driver.quit()
