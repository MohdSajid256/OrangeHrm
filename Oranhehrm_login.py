from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# OrangeHRM Demo URL
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Test credentials
USERNAME = "Admin"
PASSWORD = "admin123"

# Setup WebDriver (Make sure ChromeDriver is installed)
driver = webdriver.Firefox()

# Step 1: Open the login page
driver.get(URL)
driver.maximize_window()
time.sleep(5)

# Step 2: Enter username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(USERNAME)

# Step 3: Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)

# Step 4: Click login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(3)

title=driver.title
assert "OrangeHRM" in title

# Optional: Close the browser
driver.quit()
