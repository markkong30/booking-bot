import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time

from booking.reserve_picker import reserve_picker
from booking.login import login

# Load environment variables from .env file
load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.toyoko-inn.com/login/")

login(driver)

driver.get("https://www.toyoko-inn.com/search/detail/00175/")
driver.get("https://www.toyoko-inn.com/search/reserve/date")

reserve_picker(driver)
