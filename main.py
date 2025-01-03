from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://tryhackme.com/r/login')

browser.implicitly_wait(10)

login_field = browser.find_element(By.ID, 'username-or-email-field')
login_field.clear()
login_field.send_keys('test') 

# browser.quit()
