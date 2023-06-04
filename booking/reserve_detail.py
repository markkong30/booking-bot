from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from booking.constants import mobile_number
from booking.utils import scroll_into_view


def reserve_detail(driver: WebDriver):
    # fill mobile number
    mobile_input = driver.find_element(By.NAME, "room[0][tlpn]")
    scroll_into_view(driver, mobile_input)
    driver.find_element(By.NAME, "room[0][tlpn]").send_keys(mobile_number)

    # select check in time
    check_in_time = Select(driver.find_element(By.NAME, "room[0][checkin_tm]"))
    check_in_time.select_by_value("23:59:00")

    # add more room

    # submit booking
    submit_booking_btn = driver.find_element(By.CLASS_NAME, "jsBtnCnfrm")
    scroll_into_view(driver, submit_booking_btn)
    submit_booking_btn.click()

    # Confirm booking
    consent_checkbox = driver.find_element(By.NAME, "agreeCheck")
    scroll_into_view(driver, consent_checkbox)
    consent_checkbox.click()

    #! WARNING: THIS WILL SUBMIT THE BOOKING
    # driver.find_element(By.ID, "entry").click()
