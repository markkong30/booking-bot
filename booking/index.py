from selenium import webdriver

from booking.reserve_picker import reserve_picker
from booking.login import login
from booking.reserve_detail import reserve_detail


def initialize_booking(form_values: dict):
    print(form_values)

    hotel_id = form_values.get("hotel_id", "00175")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # login
    driver.get("https://www.toyoko-inn.com/login/")

    login(driver)

    # reserve selection
    driver.get(f"https://www.toyoko-inn.com/search/detail/{hotel_id}/")
    driver.get("https://www.toyoko-inn.com/search/reserve/date")

    reserve_picker(driver, form_values)

    # resere detail
    reserve_detail(driver, form_values)
