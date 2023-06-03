from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from booking.constants import mobile_number


def reserve_detail(driver: WebDriver):
    driver.execute_script("document.body.style.zoom='30%'")

    driver.find_element(By.NAME, "room[0][tlpn]").send_keys(mobile_number)

    check_in_time = Select(driver.find_element(By.NAME, "room[0][checkin_tm]"))
    check_in_time.select_by_value("23:59:00")
