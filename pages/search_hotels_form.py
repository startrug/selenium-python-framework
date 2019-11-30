import logging
import allure
from allure_commons.types import AttachmentType
from locators.locators import SearchHotelsFormLocators


class SearchHotelsForm:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.logger.info("Opening phptravels.net website")
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Setting destination to '{1}'")
    def set_destination(self, destination):
        self.logger.info("Setting destination: {}".format(destination))
        self.driver.find_element(*SearchHotelsFormLocators.destination_inactive).click()
        self.driver.find_element(*SearchHotelsFormLocators.destination_input).send_keys(destination)
        self.driver.find_element(*SearchHotelsFormLocators.search_match).click()

    @allure.step("Setting date range from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting date range from {checkin} to {checkout}".format(checkin=check_in, checkout=check_out))
        self.driver.find_element(*SearchHotelsFormLocators.checkin_input).click()
        self.driver.find_element(*SearchHotelsFormLocators.checkin_input).send_keys(check_in)
        self.driver.find_element(*SearchHotelsFormLocators.checkout_input).click()
        self.driver.find_element(*SearchHotelsFormLocators.checkout_input).send_keys(check_out)

    @allure.step("Setting number of adults to '{1}'")
    def set_adults_number(self, num):
        self.logger.info("Setting number of adults: {adults}".format(adults=num))
        adults_input = self.driver.find_element(*SearchHotelsFormLocators.adults_input_value)
        adults_input_val = int(adults_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchHotelsFormLocators.adults_add)
        subtract_btn = self.driver.find_element(*SearchHotelsFormLocators.adults_sub)
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

    @allure.step("Setting number of adults to '{1}'")
    def set_kids_number(self, num):
        self.logger.info("Setting number of kids: {kids}".format(kids=num))
        kids_input = self.driver.find_element(*SearchHotelsFormLocators.kids_input_value)
        kids_input_val = int(kids_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchHotelsFormLocators.kids_add)
        subtract_btn = self.driver.find_element(*SearchHotelsFormLocators.kids_sub)
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

    @allure.step("Performing search")
    def search_perform(self):
        self.logger.info("Performing search")
        self.driver.find_element(*SearchHotelsFormLocators.search_btn).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)