from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

browser = webdriver.Firefox()
browser.get('https://tryhackme.com/r/login')

def read_credentials(filename):
    with open(filename, 'r') as file:
        credentials = json.load(file)
    return credentials

def bypass_captcha(browser):
    """Bypass reCAPTCHA"""
    try:
        WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
        
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

        time.sleep(5)
    except Exception as exception:
        print("Error during CAPTCHA bypass:", exception)

def login(browser, user, mdp):
    """Whole login process"""
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

bypass_captcha(browser)

login(browser, user, mdp)
