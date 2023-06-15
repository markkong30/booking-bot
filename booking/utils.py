def scroll_into_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element


def has_empty_strings(dictionary):
    if isinstance(dictionary, dict):
        return any(has_empty_strings(value) for value in dictionary.values())
    return isinstance(dictionary, str) and dictionary == ""
