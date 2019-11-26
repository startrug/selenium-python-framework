import logging
import allure
from selenium.webdriver.support.select import Select

from locators.locators import SearchFlightsFormLocators, SearchTabsLocators


class SearchFlightsForm:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.logger.info("Opening phptravels.net website")
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Opening Flights tab")
    def open_flights_tab(self):
        self.logger.info("Opening Flights tab")
        self.driver.find_element(*SearchTabsLocators.flights_tab).click()

    @allure.step("Selecting one way trip")
    def set_one_way(self):
        self.logger.info("Selecting one way trip")
        self.driver.find_element(*SearchFlightsFormLocators.one_way_radio).click()

    @allure.step("Selecting round trip")
    def set_round_trip(self):
        self.logger.info("Selecting round trip")
        self.driver.find_element(*SearchFlightsFormLocators.round_trip_radio).click()

    @allure.step("Setting cabin class")
    def set_cabin_class(self, cabin_class):
        self.logger.info("Setting economy cabin class")
        select = Select(self.driver.find_element(*SearchFlightsFormLocators.cabinclass_select))
        select.select_by_value(cabin_class)

    @allure.step("Setting economy cabin class")
    def set_economy_class(self):
        self.logger.info("Setting economy cabin class")
        self.driver.find_element(*SearchFlightsFormLocators.cabinclass_select).click()
        self.driver.find_element(*SearchFlightsFormLocators.economy_class).click()

    @allure.step("Setting first cabin class")
    def set_first_class(self):
        self.logger.info("Setting first cabin class")
        self.driver.find_element(*SearchFlightsFormLocators.cabinclass_select).click()
        self.driver.find_element(*SearchFlightsFormLocators.first_class).click()

    @allure.step("Setting business cabin class")
    def set_business_class(self):
        self.logger.info("Setting business cabin class")
        self.driver.find_element(*SearchFlightsFormLocators.cabinclass_select).click()
        self.driver.find_element(*SearchFlightsFormLocators.business_class).click()

    @allure.step("Setting number of adults to '{1}'")
    def set_adults_number(self, num):
        self.logger.info("Setting number of adults: {adults}".format(adults=num))
        adults_input = self.driver.find_element(*SearchFlightsFormLocators.adults_input_value)
        adults_input_val = int(adults_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFlightsFormLocators.adults_add)
        subtract_btn = self.driver.find_element(*SearchFlightsFormLocators.adults_sub)
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
        kids_input = self.driver.find_element(*SearchFlightsFormLocators.kids_input_value)
        kids_input_val = int(kids_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFlightsFormLocators.kids_add)
        subtract_btn = self.driver.find_element(*SearchFlightsFormLocators.kids_sub)
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

    @allure.step("Setting number of infants to '{1}'")
    def set_infants_number(self, num):
        self.logger.info("Setting number of infants: {infants}".format(infants=num))
        infants_input = self.driver.find_element(*SearchFlightsFormLocators.infants_input_value)
        infants_input_val = int(infants_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFlightsFormLocators.infants_add)
        subtract_btn = self.driver.find_element(*SearchFlightsFormLocators.infants_sub)
        if num < infants_input_val:
            while infants_input_val > num:
                subtract_btn.click()
                infants_input_val -= 1
        elif num == infants_input_val:
            pass
        else:
            while infants_input_val < num:
                add_btn.click()
                infants_input_val += 1

    @allure.step("Performing search")
    def search_perform(self):
        self.logger.info("Performing search")
        self.driver.find_element(*SearchFlightsFormLocators.search_btn).click()