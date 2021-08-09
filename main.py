from selenium import webdriver
import time

drivers = webdriver.Chrome(executable_path='driver/chromedriver.exe')
drivers.get("https://www.google.co.in/")
time.sleep(3)

name = drivers.find_element_by_name('q').send_keys('facebook.com')
time.sleep(3)

btn = drivers.find_element_by_name('btnK').click()
time.sleep(5)

facebook = drivers.find_element_by_class_name('LC20lb').click()
time.sleep(3)

email = drivers.find_element_by_name('email').send_keys('email')
time.sleep(3)

password = drivers.find_element_by_name('pass').send_keys('password')
time.sleep(3)

drivers.find_element_by_name('login').click()
time.sleep(3)

print(drivers.title)

drivers.close()