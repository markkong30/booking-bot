from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from booking.constants import mobile_number
from booking.utils import scroll_into_view
from booking.change_room import change_room


def reserve_detail(driver: WebDriver, form_values: dict):
    # reserve room
    for k, v in form_values.items():
        if k.startswith("room"):
            reserve_room(driver, v, int(k[-1]))

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


def reserve_room(driver: WebDriver, room: dict, room_number: int):
    index = room_number - 1

    # Add room
    if room_number != 1:
        add_room_btn = driver.find_elements(By.CLASS_NAME, "addTxt")[index - 1]

        scroll_into_view(driver, add_room_btn)
        add_room_btn.click()

    # fill mobile number
    mobile_input = driver.find_element(By.NAME, f"room[{index}][tlpn]")
    scroll_into_view(driver, mobile_input)
    driver.find_element(By.NAME, f"room[{index}][tlpn]").send_keys(mobile_number)

    # select check in time
    check_in_time = Select(driver.find_element(By.NAME, f"room[{index}][checkin_tm]"))
    check_in_time.select_by_value("23:59:00")

    # change room type
    change_room(driver, room_number, room["room_type"])
