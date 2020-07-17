'''
searching for hotsring in taobao by xpath and css-selector
'''

#import webdriver
from  selenium import  webdriver
import time

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open taobao
driver.get("http://www.taobao.com")
time.sleep(2)

#search hotstring by xpath
# //*[@id="q"]
# //*[@id="J_TSearchForm"]/div[1]/button
#modify * first
driver.find_element_by_xpath('//input[@id="q"]').send_keys("hotstring")
driver.find_element_by_xpath('//form[contains(@id,"J_TSearch")]/div[1]/button').click()
time.sleep(2)

#back to homepage
driver.back()
time.sleep(2)

#search hotstring by css-selector
# < ul
# class ="nav-hd " >
# < li > < a
# href = "https://www.tmall.com" > 天猫 < / a > < / li >
# < li > < a
# href = "https://ju.taobao.com" > 聚划算 < / a > < / li >
# < li > < a
# href = "https://chaoshi.tmall.com" > 天猫超市 < / a > < / li >
# < / ul >
# driver.find_element_by_css_selector('ul[class="nav-hd "] li:nth-child(2)>a').click()
# time.sleep(2)

driver.find_element_by_css_selector('ul[class*="vice-b"] li').click()
time.sleep(2)

# driver.find_element_by_css_selector('')

driver.quit()