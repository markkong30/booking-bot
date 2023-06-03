from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from booking.constants import login_email, login_password


def login(driver: WebDriver):
    # Close the cookie dialog
    el = driver.find_element(By.CSS_SELECTOR, 'input[name="mail"]')
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 20, 20)
    action.click()
    action.perform()

    driver.find_element(By.CSS_SELECTOR, 'input[name="mail"]').send_keys(login_email)
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(
        login_password
    )

    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
