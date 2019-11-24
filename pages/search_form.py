import logging
from locators.locators import SearchFormLocators


class SearchForm:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open_page(self):
        self.logger.info("Opening phptravels.net website")
        self.driver.get("http://www.phptravels.net/")

    def set_destination(self, destination):
        self.logger.info("Setting destination: {}".format(destination))
        self.driver.find_element(*SearchFormLocators.destination_inactive).click()
        self.driver.find_element(*SearchFormLocators.destination_input).send_keys(destination)
        self.driver.find_element(*SearchFormLocators.search_match).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting date range from {'1'} to {'2'}")
        self.driver.find_element(*SearchFormLocators.checkin_input).click()
        self.driver.find_element(*SearchFormLocators.checkin_input).send_keys(check_in)
        self.driver.find_element(*SearchFormLocators.checkout_input).click()
        self.driver.find_element(*SearchFormLocators.checkout_input).send_keys(check_out)

    def set_adults_number(self, num):
        self.logger.info("Setting travellers adults - {adults}".format(adults=num))
        adults_input = self.driver.find_element(*SearchFormLocators.adults_input_value)
        adults_input_val = int(adults_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFormLocators.adults_add)
        subtract_btn = self.driver.find_element(*SearchFormLocators.adults_sub)
        if num < adults_input_val:
            while adults_input_val > num:
                subtract_btn.click()
                adults_input_val -= 1
        elif num == adults_input_val:
            pass
        else:
            while adults_input_val < num:
                add_btn.click()
                adults_input_val += 1

    def set_kids_number(self, num):
        self.logger.info("Setting travellers kids - {kids}".format(kids=num))
        kids_input = self.driver.find_element(*SearchFormLocators.kids_input_value)
        kids_input_val = int(kids_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFormLocators.kids_add)
        subtract_btn = self.driver.find_element(*SearchFormLocators.kids_sub)
        if num < kids_input_val:
            while kids_input_val > num:
                subtract_btn.click()
                kids_input_val -= 1
        elif num == kids_input_val:
            pass
        else:
            while kids_input_val < num:
                add_btn.click()
                kids_input_val += 1

    def search_perform(self):
        self.logger.info("Performing search")
        self.driver.find_element(*SearchFormLocators.search_btn).click()