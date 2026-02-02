import time
from logging.config import IDENTIFIER
from selenium.webdriver.common.by import By

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://practicetestautomation.com/practice-test-login/")
print("Open Browser")
title = browser.title
print(title)
browser.minimize_window()
username = browser.find_element(By.ID, "username")
username.send_keys("student")
time.sleep(200)

