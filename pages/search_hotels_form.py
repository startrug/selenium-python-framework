import allure
from allure_commons.types import AttachmentType
from locators.locators import SearchHotelsFormLocators
from utils.functions import set_travellers_number


class SearchHotelsForm:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Setting destination to '{1}'")
    def set_destination(self, destination):
        self.driver.find_element(*SearchHotelsFormLocators.destination_inactive).click()
        self.driver.find_element(*SearchHotelsFormLocators.destination_input).send_keys(destination)
        self.driver.find_element(*SearchHotelsFormLocators.search_match).click()

    @allure.step("Setting date range from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        self.driver.find_element(*SearchHotelsFormLocators.checkin_input).click()
        self.driver.find_element(*SearchHotelsFormLocators.checkin_input).send_keys(check_in)
        self.driver.find_element(*SearchHotelsFormLocators.checkout_input).click()
        self.driver.find_element(*SearchHotelsFormLocators.checkout_input).send_keys(check_out)

    @allure.step("Setting number of adults to '{1}'")
    def set_adults_number(self, adults_num):
        set_travellers_number(self.driver, adults_num, SearchHotelsFormLocators,
                              ["adults_input_value", "adults_add", "adults_sub"])

    @allure.step("Setting number of adults to '{1}'")
    def set_kids_number(self, kids_num):
        set_travellers_number(self.driver, kids_num, SearchHotelsFormLocators,
                              ["kids_input_value", "kids_add", "kids_sub"])

    @allure.step("Performing search")
    def search_perform(self):
        self.driver.find_element(*SearchHotelsFormLocators.search_btn).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)
