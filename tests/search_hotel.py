import pytest
import allure

from pages.search_form import SearchForm


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Search hotel test")
    @allure.description("This is test of searching hotel in Warsaw")
    def test_search_hotel(self, setup):
        search_hotel = SearchForm(self.driver)
        search_hotel.open_page()
        search_hotel.set_destination("Warsaw")
        search_hotel.set_date_range("29/12/2019", "03/01/2020")
        search_hotel.search_perform()
