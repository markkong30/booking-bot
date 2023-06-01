import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def login(driver: WebDriver):
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
