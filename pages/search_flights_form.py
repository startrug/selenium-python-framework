import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

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

    @allure.step("Selecting trip type to: '{1}'")
    def set_trip_type(self, trip_type):
        self.logger.info(f"Selecting trip type to: '{trip_type}'")
        self.driver.find_element(By.XPATH, f"//label[text()='{trip_type}']").click()

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
        self.logger.info("Setting cabin class")
        self.driver.find_element(*SearchFlightsFormLocators.cabinclass_dropdown).click()
        self.driver.find_element(By.XPATH, f"//li[text()='{cabin_class}']").click()

    @allure.step("Setting location from: '{1}'")
    def set_loc_from(self, loc_from):
        self.logger.info(f"Setting location from: {loc_from}")
        self.driver.find_element(*SearchFlightsFormLocators.loc_from_inactive).click()
        self.driver.find_element(*SearchFlightsFormLocators.loc_input_active).send_keys(loc_from)
        self.driver.find_element(By.XPATH, f"//div[@class='select2-result-label'][contains(.,'({loc_from})')]").click()

    @allure.step("Setting location to: '{1}'")
    def set_loc_to(self, loc_to):
        self.logger.info(f"Setting location to: {loc_to}")
        self.driver.find_element(*SearchFlightsFormLocators.loc_to_inactive).click()
        self.driver.find_element(*SearchFlightsFormLocators.loc_input_active).send_keys(loc_to)
        self.driver.find_element(By.XPATH, f"//div[@class='select2-result-label'][contains(.,'({loc_to})')]").click()

    @allure.step("Setting start date to '{1}'/'{2}'/'{3}'")
    def set_start_date(self, start_year, start_month, start_day):
        self.logger.info(f"Setting start date to {start_year}/{start_month}/{start_day}")
        self.driver.find_element(*SearchFlightsFormLocators.flight_date_start).click()
        current_year = ""
        years = self.driver.find_elements(By.XPATH, "//div[@class='datepicker--nav-title']//i")
        for year in years:
            if year.is_displayed():
                current_year = year.text
                break
        if current_year != start_year:
            self.driver.find_element(*SearchFlightsFormLocators.datepicker_nav_title_start).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{start_year}')]").click()
        else:
            pass
        current_month = ""
        months = self.driver.find_elements(By.XPATH, "//div[@class='datepicker--nav-title']")
        for month in months:
            if month.is_displayed():
                current_month = month.text
                break
        if current_month[0:3] != start_month:
            self.driver.find_element(By.XPATH, f"//div[contains(@class,'cell-month')]"
                                               f"[contains(.,'{start_month}')]").click()
        else:
            pass
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{start_day}']")
        for day in days:
            if day.is_displayed():
                day.click()
                break
        start_date = self.driver.find_element(*SearchFlightsFormLocators.flight_date_start)
        start_date_val = start_date.get_attribute("value")
        print("Start date is: " + start_date_val)

    def set_end_date(self, end_year, end_month, end_day):
        self.logger.info(f"Setting end date to {end_year}/{end_month}/{end_day}")
        current_year = ""
        current_month = ""
        years = self.driver.find_elements(By.XPATH, "//div[@class='datepicker--nav-title']//i")
        months = self.driver.find_elements(By.XPATH, "//div[@class='datepicker--nav-title']")
        for year in years:
            if year.is_displayed():
                current_year = year.text
                break
        for month in months:
            if month.is_displayed():
                current_month = month.text
                break
        if end_year != current_year:
            self.driver.find_element(*SearchFlightsFormLocators.datepicker_nav_title_end).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{end_year}')]").click()
        else:
            pass
        if current_month[0:3] != end_month and current_year == end_year:
            self.driver.find_element(*SearchFlightsFormLocators.datepicker_nav_title_end).click()
            print("metoda 1")
            months = self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{end_month}')]")
            for month in months:
                if month.is_displayed():
                    month.click()
                    break
        else:
            pass
        if current_month[0:3] != end_month and current_year != end_year:
            print("metoda 1")
            months = self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{end_month}')]")
            for month in months:
                if month.is_displayed():
                    month.click()
                    break
        else:
            pass
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{end_day}']")
        for day in days:
            if day.is_displayed():
                day.click()
                break
        end_date = self.driver.find_element(*SearchFlightsFormLocators.flight_date_end)
        end_date_val = end_date.get_attribute("value")
        print("End date is: ", end_date_val)

    @allure.step("Setting number of adults to '{1}'")
    def set_adults_number(self, adults_num):
        self.logger.info(f"Setting number of adults: {adults_num}")
        adults_input = self.driver.find_element(*SearchFlightsFormLocators.adults_input_value)
        adults_input_val = int(adults_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFlightsFormLocators.adults_add)
        subtract_btn = self.driver.find_element(*SearchFlightsFormLocators.adults_sub)
        if adults_num < adults_input_val:
            while adults_input_val > adults_num:
                subtract_btn.click()
                adults_input_val -= 1
        elif adults_num == adults_input_val:
            pass
        else:
            while adults_input_val < adults_num:
                add_btn.click()
                adults_input_val += 1

    @allure.step("Setting number of adults to '{1}'")
    def set_kids_number(self, kids_num):
        self.logger.info(f"Setting number of kids: {kids_num}")
        kids_input = self.driver.find_element(*SearchFlightsFormLocators.kids_input_value)
        kids_input_val = int(kids_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFlightsFormLocators.kids_add)
        subtract_btn = self.driver.find_element(*SearchFlightsFormLocators.kids_sub)
        if kids_num < kids_input_val:
            while kids_input_val > kids_num:
                subtract_btn.click()
                kids_input_val -= 1
        elif kids_num == kids_input_val:
            pass
        else:
            while kids_input_val < kids_num:
                add_btn.click()
                kids_input_val += 1

    @allure.step("Setting number of infants to '{1}'")
    def set_infants_number(self, infants_num):
        self.logger.info(f"Setting number of infants: {infants_num}")
        infants_input = self.driver.find_element(*SearchFlightsFormLocators.infants_input_value)
        infants_input_val = int(infants_input.get_attribute("value"))
        add_btn = self.driver.find_element(*SearchFlightsFormLocators.infants_add)
        subtract_btn = self.driver.find_element(*SearchFlightsFormLocators.infants_sub)
        if infants_num < infants_input_val:
            while infants_input_val > infants_num:
                subtract_btn.click()
                infants_input_val -= 1
        elif infants_num == infants_input_val:
            pass
        else:
            while infants_input_val < infants_num:
                add_btn.click()
                infants_input_val += 1

    @allure.step("Performing search")
    def search_perform(self):
        self.logger.info("Performing search")
        self.driver.find_element(*SearchFlightsFormLocators.search_btn).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)
