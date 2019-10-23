from selenium import webdriver
import re
import time

link = 'http://172.16.95.117/bugfree/'
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(link)

username = driver.find_element_by_name('TestUserName')
username.clear()
username.send_keys('zhoudawei')

password = driver.find_element_by_name('TestUserPWD')
password.clear()
password.send_keys('zhoudawei')

submit = driver.find_element_by_id('SubmitLoginBTN')
submit.click()

time.sleep(5)
driver.quit()
