'''
case:searching practice in ecshop back page(add user)
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time

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

#add user(method1)
# #/html/frameset
# # driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame[1]'))
# driver.switch_to.frame('header-frame')
# #//*[@id="menu-div"]/ul/li[11]/a会员列表
# driver.find_element(By.XPATH,'//div[@id="menu-div"]/ul/li[11]/a').click()
# time.sleep(1)
# driver.switch_to.parent_frame()
# driver.switch_to.frame('main-frame')
# #/html/body/h1/span[1]/a添加会员
# driver.find_element(By.XPATH,'//span[@class="action-span"]/a').click()
# driver.find_element_by_name('username').send_keys('wanghh')
# driver.find_element_by_name('email').send_keys('111@qq.com')
# driver.find_element_by_name('password').send_keys('123456')
# driver.find_element_by_name('confirm_password').send_keys('123456')
# driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[14]/td/input[1]').click()
# time.sleep(3)

#add user(method2)
driver.switch_to.frame('menu-frame')
# #//*[@id="menu-ul"]/li[7]
# #//*[@id="menu-ul"]/li[7]/ul/li[2]/a
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]/ul/li[2]/a').click()
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
driver.find_element_by_name('username').send_keys('wangxx')
driver.find_element_by_name('email').send_keys('999@qq.com')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_name('confirm_password').send_keys('123456')
driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[14]/td/input[1]').click()
time.sleep(3)

#close and quit
time.sleep(2)
driver.quit()