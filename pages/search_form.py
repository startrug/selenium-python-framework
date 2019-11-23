from locators.locators import SearchFormLocators


class SearchForm:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    def set_destination(self, destination):
        self.driver.find_element(*SearchFormLocators.destination_inactive).click()
        self.driver.find_element(*SearchFormLocators.destination_input).send_keys(destination)

    def set_date_range(self, checkin, checkout):
        self.driver.find_element(*SearchFormLocators.checkin_input).send_keys(checkin)
        self.driver.find_element(*SearchFormLocators.checkout_input).send_keys(checkout)

    def search_perform(self):
        self.driver.find_element(*SearchFormLocators.search_btn).click()