def scroll_into_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element
