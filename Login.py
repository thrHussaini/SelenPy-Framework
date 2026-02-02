from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
url= "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
username_enter = "student"
password_enter = "Password123"
username = driver.find_element(By.ID, "username")
username.send_keys(username_enter)
password = driver.find_element(By.ID, "password")
password.send_keys(password_enter)