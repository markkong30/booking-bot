from selenium import webdriver

from booking.reserve_picker import reserve_picker
from booking.login import login
from booking.reserve_detail import reserve_detail


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument(f"--force-device-scale-factor={0.5}")
# options.add_argument("high-dpi-support=0.5")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)


# login
driver.get("https://www.toyoko-inn.com/login/")

login(driver)

# reserve selection
driver.get("https://www.toyoko-inn.com/search/detail/00175/")
driver.get("https://www.toyoko-inn.com/search/reserve/date")

reserve_picker(driver)


# resere detail

reserve_detail(driver)
