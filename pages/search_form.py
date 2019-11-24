from locators.locators import SearchFormLocators


class SearchForm:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    def set_destination(self, destination):
        self.driver.find_element(*SearchFormLocators.destination_inactive).click()
        self.driver.find_element(*SearchFormLocators.destination_input).send_keys(destination)
        self.driver.find_element(*SearchFormLocators.search_match).click()

    def set_date_range(self, checkin, checkout):
        self.driver.find_element(*SearchFormLocators.checkin_input).click()
        self.driver.find_element(*SearchFormLocators.checkin_input).send_keys(checkin)
        self.driver.find_element(*SearchFormLocators.checkout_input).click()
        self.driver.find_element(*SearchFormLocators.checkout_input).send_keys(checkout)

    def set_adults_number(self, num):
        if num < 2:
            subtract_btn = self.driver.find_element(*SearchFormLocators.adults_sub)
            adults_input_val = self.driver.find_element(*SearchFormLocators.adults_input_value)
            while int(adults_input_val.get_attribute("readonly value")) > num:
                subtract_btn.click()
                adults_input_val -= 1
        elif num == 2:
            pass
        else:
            add_btn = self.driver.find_element(*SearchFormLocators.adults_add)
            adults_input_val = self.driver.find_element(*SearchFormLocators.adults_input_value)
            while int(adults_input_val.get_attribute("readonly value")) < num:
                add_btn.click()
                adults_input_val += 1

    def search_perform(self):
        self.driver.find_element(*SearchFormLocators.search_btn).click()