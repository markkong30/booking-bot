from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from constants import Smoking_type, No_of_people, Room_type


def reserve_picker(driver: WebDriver):
    date_picker = driver.find_element(By.ID, "datepicker02")
    date_picker.click()
    date_picker.send_keys("20231102", Keys.ENTER)

    number_of_people = Select(driver.find_element(By.NAME, "rmnd_ppl"))
    number_of_people.select_by_value(No_of_people.TWO)

    smoking_type = Select(driver.find_element(By.NAME, "smkng_type"))
    smoking_type.select_by_value(Smoking_type.NON_SMOKING)

    room_type = Select(driver.find_element(By.NAME, "room_type"))
    room_type.select_by_value(Room_type.DOUBLE)

    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    room = driver.find_element(By.XPATH, '//*[@id="tbody_std"]/tr[2]/td[4]/a')
    room.click()
