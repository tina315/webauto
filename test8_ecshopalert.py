'''
case:alert practice in ecshop front page
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
driver.get("http://localhost/upload/index.php")
time.sleep(2)

#点击收藏本站并接受
driver.find_element(By.LINK_TEXT,'收藏本站').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
#点击收藏本站并取消
driver.find_element(By.LINK_TEXT,'收藏本站').click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
#对于alert类的弹框，accept与dismiss是一样的效果

#close and quit
driver.quit()