from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

from booking.utils import scroll_into_view
from booking.constants import Room_type_text


def change_room(driver: WebDriver, room_number: int, room_type_entry: str):
    # change room type
    change_room_btn = driver.find_element(
        By.CSS_SELECTOR, f".jsLinkRoom:nth-of-type({room_number})"
    )
    scroll_into_view(driver, change_room_btn)
    change_room_btn.click()

    modal = driver.find_element(By.CSS_SELECTOR, "#cboxLoadedContent > iframe")
    driver.switch_to.frame(modal)

    room_type = driver.find_element(
        By.XPATH, f"//*[text()='{Room_type_text[room_type_entry.upper()].value}']"
    )
    room_type.click()

    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    driver.switch_to.default_content()
    time.sleep(2)
