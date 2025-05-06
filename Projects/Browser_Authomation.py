# The purpose of this code is to automate
# the process of logging into a GitHub account
# using a web browser. Instead of manually opening a browser,
# navigating to GitHub, and typing your username and password,
# this script does it all for you automatically.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.github.com")

signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

time.sleep(2)

# Note: Replace "my_username" and "my_password"
# with your actual GitHub credentials for the script
# to function correctly.

username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys("my_username")  # replace with your username
password_box = browser.find_element(By.ID, "password")
password_box.send_keys("my_password")  # replace with your password
password_box.submit()

time.sleep(2)

profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "my_usernam" in link_label

browser.quit()
