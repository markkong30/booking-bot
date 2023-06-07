from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from booking.constants import Smoking_type, No_of_people, Room_type


def reserve_picker(driver: WebDriver, form_values: dict):
    date = form_values.get("date")
    number_of_people_entry, room_type_entry = form_values["room_1"].values()

    date_picker = driver.find_element(By.ID, "datepicker02")
    date_picker.click()
    date_picker.send_keys(date, Keys.ENTER)

    number_of_people = Select(driver.find_element(By.NAME, "rmnd_ppl"))
    number_of_people.select_by_value(number_of_people_entry)

    smoking_type = Select(driver.find_element(By.NAME, "smkng_type"))
    smoking_type.select_by_value(Smoking_type.NON_SMOKING.value)

    room_type = Select(driver.find_element(By.NAME, "room_type"))
    room_type.select_by_value(Room_type[room_type_entry.upper()].value)

    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    default_room = driver.find_element(By.XPATH, '//*[@id="tbody_std"]/tr[1]/td[4]/a')
    default_room.click()
