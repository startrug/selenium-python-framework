import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from locators.locators import SearchTabsLocators, SearchTransferLocators
from utils.functions import get_datestamp, click_displayed_datestamp


class SearchTransfersForm:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Opening Transfer tab")
    def open_transfer_tab(self):
        self.driver.find_element(*SearchTabsLocators.transfer_tab).click()

    @allure.step("Setting pick up location: '{1}'")
    def set_pick_up_loc(self, pick_up_loc):
        self.driver.find_element(*SearchTransferLocators.pick_up_loc).click()
        self.driver.find_element(By.XPATH, f"//li[contains(text(),'{pick_up_loc}')]").click()

    @allure.step("Setting drop off location: '{1}'")
    def set_drop_off_loc(self, drop_off_loc):
        self.driver.find_element(*SearchTransferLocators.drop_off_loc).click()
        loc_select = Select(self.driver.find_element(*SearchTransferLocators.drop_off_loc))
        loc_select.select_by_visible_text(drop_off_loc)

    @allure.step("Setting depart date to '{1}'/'{2}'/'{3}'")
    def set_depart_date(self, start_year, start_month, start_day):
        self.driver.find_element(*SearchTransferLocators.depart_date).click()
        current_year = get_datestamp(self.driver, SearchTransferLocators, ["datepicker_nav_title_years"])
        if current_year != start_year:
            self.driver.find_element(*SearchTransferLocators.datepicker_nav_title_start).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{start_year}')]").click()
        current_month = get_datestamp(self.driver, SearchTransferLocators, ["datepicker_nav_title_months"])
        if current_month[0:3] != start_month:
            self.driver.find_element(By.XPATH, f"//div[contains(@class,'cell-month')]"
                                               f"[contains(.,'{start_month}')]").click()
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{start_day}']")
        click_displayed_datestamp(days)

    @allure.step("Setting depart time to '{depart_time}'")
    def set_depart_time(self, depart_time):
        self.driver.find_element(*SearchTransferLocators.depart_time_selector).click()
        self.driver.find_element(*SearchTransferLocators.depart_time_imput).send_keys(depart_time, Keys.ENTER)

    @allure.step("Setting return date to '{1}'/'{2}'/'{3}'")
    def set_return_date(self, end_year, end_month, end_day):
        self.driver.find_element(*SearchTransferLocators.return_date).click()
        current_year = get_datestamp(self.driver, SearchTransferLocators, ["datepicker_nav_title_years"])
        if current_year != end_year:
            self.driver.find_element(*SearchTransferLocators.datepicker_nav_title_end).click()
            self.driver.find_element(By.XPATH, f"//div[text()='{current_year}']").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{end_year}')]").click()
        current_month = get_datestamp(self.driver, SearchTransferLocators, ["datepicker_nav_title_months"])
        if current_month[0:3] != end_month and current_year == end_year:
            self.driver.find_element(*SearchTransferLocators.datepicker_nav_title_end).click()
            months = self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{end_month}')]")
            click_displayed_datestamp(months)
        if current_month[0:3] != end_month and current_year != end_year:
            months = self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{end_month}')]")
            click_displayed_datestamp(months)
        days = self.driver.find_elements(By.XPATH, f"//div[contains(@class,'cell-day')]"
                                                   f"[text()='{end_day}']")
        click_displayed_datestamp(days)

    @allure.step("Setting return time to '{return_time}'")
    def set_return_time(self, return_time):
        self.driver.find_element(*SearchTransferLocators.return_time_selector).click()
        self.driver.find_element(*SearchTransferLocators.return_time_input).send_keys(return_time, Keys.ENTER)

    @allure.step("Performing search")
    def search_perform(self):
        self.driver.find_element(*SearchTransferLocators.search_btn).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)
