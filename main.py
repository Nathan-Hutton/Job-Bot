import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv('/Users/natha/PycharmProjects/info.env') # Path to your environment variables file goes here

service = Service("C:\important\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=90000716&keywords=python%20developer&location=Salt%20Lake%20City%20Metropolitan%20Area')

time.sleep(3.5)
sign_in = driver.find_element(By.CSS_SELECTOR, '.cta-modal a')
sign_in.click()
username = driver.find_element(By.ID, 'username')
username.send_keys(os.getenv('MY_EMAIL') + Keys.TAB + os.getenv('LINKEDIN_PASSWORD') + Keys.ENTER)
time.sleep(2)
links = driver.find_elements(By.CLASS_NAME, 'job-card-list__title')
for link in links:
    link.click()
    time.sleep(2)
    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
    except selenium.common.exceptions.NoSuchElementException:
        continue
    easy_apply_button.click()
    continue_button = driver.find_element(By.CSS_SELECTOR, '.display-flex button')
    continue_button.click()
    button = driver.find_elements(By.CLASS_NAME, 'display-flex button')[3]
    if button.text == 'Next':
        close = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        close.click()
        confirm = driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')
        confirm.click()
        continue
    else:
        button.click()
        break
    # submit = driver.find_elements(By.CSS_SELECTOR, '.display-flex button')[3]
    # submit.click()
