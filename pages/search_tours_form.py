import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import SearchTabsLocators, SearchToursFormLocators
from utils.functions import set_travellers_number, get_datestamp, click_displayed_datestamp


class SearchToursForm:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Opening Tours tab")
    def open_tours_tab(self):
        self.driver.find_element(*SearchTabsLocators.tours_tab).click()

    @allure.step("Setting tour destination: '{1}'")
    def set_tour_destination(self, tour_destination):
        self.driver.find_element(*SearchToursFormLocators.tour_destination_inactive).click()
        self.driver.find_element(*SearchToursFormLocators.tour_destination_active).send_keys(tour_destination)
        self.driver.find_element(By.XPATH, f"//div[@class='select2-result-label']"
                                           f"[contains(.,'{tour_destination}')]").click()

    @allure.step("Setting tour type: '{1}'")
    def set_tour_type(self, tour_type):
        self.driver.find_element(*SearchToursFormLocators.tour_type_dropdown).click()
        self.driver.find_element(*SearchToursFormLocators.tour_type_input).send_keys(tour_type, Keys.ENTER)

    @allure.step("Setting tour date to '{1}'/'{2}'/'{3}'")
    def set_date(self, start_year, start_month, start_day):
        self.driver.find_element(*SearchToursFormLocators.tour_date).click()
        current_year = get_datestamp(self.driver, SearchToursFormLocators, ["datepicker_nav_title_years"])
        if current_year != start_year:
            self.driver.find_element(*SearchToursFormLocators.datepicker_nav_title_start).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{start_year}')]").click()
        current_month = get_datestamp(self.driver, SearchToursFormLocators, ["datepicker_nav_title_months"])
        if current_month[0:3] != start_month:
            self.driver.find_element(By.XPATH, f"//div[contains(@class,'cell-month')]"
                                               f"[contains(.,'{start_month}')]").click()
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{start_day}']")
        click_displayed_datestamp(days)

    @allure.step("Setting number of adults to '{1}'")
    def set_adults_number(self, adults_num):
        set_travellers_number(self.driver, adults_num, SearchToursFormLocators,
                              ["adults_input_value", "adults_add", "adults_sub"])

    @allure.step("Performing search")
    def search_perform(self):
        self.driver.find_element(*SearchToursFormLocators.search_btn).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)
