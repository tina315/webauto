#webauto practice1

#import weddriver
from selenium import webdriver
import time

#start chrome
driver = webdriver.Chrome()
#set window max
driver.maximize_window()

#open baidu
driver.get("http://www.baidu.com")
#wait 3 second
time.sleep(3)
#refresh
driver.refresh()

#open taobao
driver.get("http://www.taobao.com")
#wait 2 second
time.sleep(2)

#open jd
driver.get("http://www.jd.com")
#wait 2 second
time.sleep(2)

#back to taobao
driver.back()
#set window size
driver.set_window_size(1666,1000)
#wait 2 second
time.sleep(2)

#back to baidu
driver.back()
#wait 2 second
time.sleep(2)

#forward taobao
driver.forward()
#wait 2 second
time.sleep(2)

#forward jd
driver.forward()
#wait 2 second
time.sleep(2)

#close url
#driver.close()

#close and quit webdriver
driver.quit()