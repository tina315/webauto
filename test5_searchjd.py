'''
search for hotstring in jd by BY
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open jd
driver.get("http://www.jd.com")
time.sleep(2)

# #search for hotstring
# driver.find_element(By.ID,"key").send_keys("辣条")
# driver.find_element(By.CLASS_NAME,"button").click()
# time.sleep(2)
#
# #print url
# print(driver.current_url)
#
# #get in weilong
# driver.find_element(By.LINK_TEXT,"li[di$='102806']>a").click()
# time.sleep(3)

# #get in weilong
# driver.find_element(By.CSS_SELECTOR,"li[di$='102806']>a").click()
# time.sleep(3)

#search for huawei
driver.find_element(By.ID,"key").send_keys("华为手机")
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(2)

#print url
print(driver.current_url)

#重新搜索小米
driver.find_element(By.ID,"key").clear()
driver.find_element(By.ID,"key").send_keys("小米")
driver.find_element(By.XPATH,'//div[@class="form"]/button').click()
time.sleep(2)

#找到第二个商品并进入详情页
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()
time.sleep(2)

#获取价格
# /html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,'span[class="p-price"] span:nth-child(2)').text)

#加入购物车
driver.find_element_by_id("InitCartUrl").click()
time.sleep(2)

# # #查看商品详情，这时会重新开启一个窗口
# driver.find_element_by_class_name("btn-tobback").click()
# time.sleep(2)

#重新回到搜索页面
# handles = driver.window_handles
driver.switch_to.window(handles[0])

#重新搜索华为
driver.find_element(By.ID,"key").clear()
driver.find_element(By.ID,"key").send_keys("华为")
driver.find_element(By.XPATH,'//div[@class="form"]/button').click()
time.sleep(2)

#进入第3个商品页面获取价格，这时会新开一个页面(这一次就要求登录了）
# //div[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[3]/div/div[1]/a/img').click()
time.sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,'span[class="p-price"] span:nth-child(2)').text)

#加入购物车
driver.find_element_by_id("InitCartUrl").click()
time.sleep(2)

time.sleep(5)
driver.quit()