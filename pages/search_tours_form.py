import logging
import pytest
import allure
from selenium.webdriver.common.by import By

from locators.locators import SearchTabsLocators, SearchToursFormLocators


class SearchToursForm:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Opening phptravels.net website")
    def open_page(self):
        self.logger.info("Opening phptravels.net website")
        self.driver.get("http://www.phptravels.net/")

    @allure.step("Opening Tours tab")
    def open_tours_tab(self):
        self.logger.info("Opening Tours tab")
        self.driver.find_element(*SearchTabsLocators.tours_tab).click()

    @allure.step("Setting tour destination: '{1}'")
    def set_tour_destination(self, tour_destination):
        self.logger.info(f"Setting tour destination to: {tour_destination}")
        self.driver.find_element(*SearchToursFormLocators.tour_destination_inactive).click()
        self.driver.find_element(*SearchToursFormLocators.tour_destination_active).send_keys(tour_destination)
        self.driver.find_element(By.XPATH, f"//div[@class='select2-result-label']"
                                           f"[contains(.,'{tour_destination}')]").click()
