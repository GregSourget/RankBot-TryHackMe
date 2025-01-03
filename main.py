from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

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

    except Exception as exception:
        print("Error during CAPTCHA bypass:", exception)
    
    # temp

    bouton_login = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Log In']"))
    )
    bouton_login.click()

def login(browser, mail, mdp):
    """Whole login process"""
    login_field = browser.find_element(By.ID, 'username-or-email-field')
    login_field.clear()
    login_field.send_keys(mail)

    password_field = browser.find_element(By.ID, 'password-field')
    password_field.clear()
    password_field.send_keys(mdp)

    # password_field.send_keys(Keys.RETURN)

credentials = read_credentials('credentials.json')
print(credentials)

mail = credentials['mail']
mdp = credentials['password']

login(browser, mail, mdp)

bypass_captcha(browser)