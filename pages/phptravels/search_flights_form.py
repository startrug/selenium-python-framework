import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from locators.locators import SearchFlightsFormLocators, SearchTabsLocators
from utils.functions import set_travellers_number, get_datestamp, click_displayed_datestamp


class SearchFlightsForm:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Opening Flights tab")
    def open_flights_tab(self):
        self.driver.find_element(*SearchTabsLocators.flights_tab).click()

    @allure.step("Selecting trip type to: '{1}'")
    def set_trip_type(self, trip_type):
        self.driver.find_element(By.XPATH, f"//label[text()='{trip_type}']").click()

    @allure.step("Selecting one way trip")
    def set_one_way(self):
        self.driver.find_element(*SearchFlightsFormLocators.one_way_radio).click()

    @allure.step("Selecting round trip")
    def set_round_trip(self):
        self.driver.find_element(*SearchFlightsFormLocators.round_trip_radio).click()

    @allure.step("Setting cabin class")
    def set_cabin_class(self, cabin_class):
        self.driver.find_element(*SearchFlightsFormLocators.cabinclass_dropdown).click()
        self.driver.find_element(By.XPATH, f"//li[text()='{cabin_class}']").click()

    @allure.step("Setting location from: '{1}'")
    def set_loc_from(self, loc_from):
        self.driver.find_element(*SearchFlightsFormLocators.loc_from_inactive).click()
        self.driver.find_element(*SearchFlightsFormLocators.loc_input_active).send_keys(loc_from)
        self.driver.find_element(By.XPATH, f"//div[@class='select2-result-label'][contains(.,'({loc_from})')]").click()

    @allure.step("Setting location to: '{1}'")
    def set_loc_to(self, loc_to):
        self.driver.find_element(*SearchFlightsFormLocators.loc_to_inactive).click()
        self.driver.find_element(*SearchFlightsFormLocators.loc_input_active).send_keys(loc_to)
        self.driver.find_element(By.XPATH, f"//div[@class='select2-result-label'][contains(.,'({loc_to})')]").click()

    @allure.step("Setting start date to '{1}'/'{2}'/'{3}'")
    def set_start_date(self, start_year, start_month, start_day):
        self.driver.find_element(*SearchFlightsFormLocators.flight_date_start).click()
        current_year = get_datestamp(self.driver, SearchFlightsFormLocators, ["datepicker_nav_title_years"])
        if current_year != start_year:
            self.driver.find_element(*SearchFlightsFormLocators.datepicker_nav_title_start).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{start_year}')]").click()
        current_month = get_datestamp(self.driver, SearchFlightsFormLocators, ["datepicker_nav_title_months"])
        if current_month[0:3] != start_month:
            self.driver.find_element(By.XPATH, f"//div[contains(@class,'cell-month')]"
                                               f"[contains(.,'{start_month}')]").click()
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{start_day}']")
        click_displayed_datestamp(days)

    @allure.step("Setting end date to '{1}'/'{2}'/'{3}'")
    def set_end_date(self, end_year, end_month, end_day):
        current_year = get_datestamp(self.driver, SearchFlightsFormLocators, ["datepicker_nav_title_years"])
        if current_year != end_year:
            self.driver.find_element(*SearchFlightsFormLocators.datepicker_nav_title_end).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{end_year}')]").click()
        current_month = get_datestamp(self.driver, SearchFlightsFormLocators, ["datepicker_nav_title_months"])
        if current_month[0:3] != end_month and current_year == end_year:
            self.driver.find_element(*SearchFlightsFormLocators.datepicker_nav_title_end).click()
            months = self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{end_month}')]")
            click_displayed_datestamp(months)
        if current_month[0:3] != end_month and current_year != end_year:
            months = self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{end_month}')]")
            click_displayed_datestamp(months)
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{end_day}']")
        click_displayed_datestamp(days)

    @allure.step("Setting number of adults to '{1}'")
    def set_adults_number(self, adults_num):
        set_travellers_number(self.driver, adults_num, SearchFlightsFormLocators,
                              ["adults_input_value", "adults_add", "adults_sub"])

    @allure.step("Setting number of adults to '{1}'")
    def set_kids_number(self, kids_num):
        set_travellers_number(self.driver, kids_num, SearchFlightsFormLocators,
                              ["kids_input_value", "kids_add", "kids_sub"])

    @allure.step("Setting number of infants to '{1}'")
    def set_infants_number(self, infants_num):
        set_travellers_number(self.driver, infants_num, SearchFlightsFormLocators,
                              ["infants_input_value", "infants_add", "infants_sub"])

    @allure.step("Performing search")
    def search_perform(self):
        self.driver.find_element(*SearchFlightsFormLocators.search_btn).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)

    @allure.step("Getting input start date")
    def get_start_date(self):
        start_date = self.driver.find_element(*SearchFlightsFormLocators.flight_date_start)
        start_date_val = start_date.get_attribute("value")

    @allure.step("Getting input end date")
    def get_end_date(self):
        end_date = self.driver.find_element(*SearchFlightsFormLocators.flight_date_end)
        end_date_val = end_date.get_attribute("value")
