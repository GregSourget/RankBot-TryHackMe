from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

browser = webdriver.Firefox()
browser.get('https://tryhackme.com/r/login')

def read_credentials(filename):
    with open(filename, 'r') as file:
        credentials = json.load(file)
    return credentials

def login(browser, user, mdp):
    login_field = browser.find_element(By.ID, 'username-or-email-field')
    login_field.clear()
    login_field.send_keys(user)

    password_field = browser.find_element(By.ID, 'password-field')
    password_field.clear()
    password_field.send_keys(mdp)

    password_field.send_keys(Keys.RETURN)

credentials = read_credentials('credentials.json')
print(credentials)

user = credentials['login']
mdp = credentials['password']

login(browser, user, mdp)
print("test")

