import pytest
import allure

from locators.locators import SearchResultsLocators
from pages.search_form import SearchForm


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Search hotel test")
    @allure.description("This is test of searching hotel in Warsaw")
    def test_search_hotel(self):
        search_hotel = SearchForm(self.driver)
        search_hotel.open_page()
        search_hotel.set_destination("Warsaw")
        search_hotel.set_date_range("29/12/2019", "03/01/2020")
        search_hotel.set_adults_number(2)
        search_hotel.set_kids_number(3)
        search_hotel.search_perform()

        results_title = "Warsaw"
        assert results_title in self.driver.find_element(*SearchResultsLocators.search_title).text
