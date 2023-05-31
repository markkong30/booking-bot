import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.toyoko-inn.com/login/")

# Close the cookie dialog
el = driver.find_element(By.CSS_SELECTOR, 'input[name="mail"]')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el, 20, 20)
action.click()
action.perform()

driver.find_element(By.CSS_SELECTOR, 'input[name="mail"]').send_keys(
    os.environ["TOYOKO_EMAIL"]
)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(
    os.environ["TOYOKO_PASSWORD"]
)

driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
