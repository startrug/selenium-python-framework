import pytest
import allure

from locators.locators import SearchResultsLocators
from pages.phptravels.search_hotels_form import SearchHotelsForm
from utils.read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestHotelSearch:
    @allure.title("Search hotel test")
    @allure.description("This is test of searching hotel in Warsaw")
    def test_search_hotel_1(self):
        search_hotel = SearchHotelsForm(self.driver)
        search_hotel.open_page()
        search_hotel.set_destination("Warsaw")
        search_hotel.set_date_range("29/12/2019", "03/01/2020")
        search_hotel.set_adults_number(3)
        search_hotel.set_kids_number(0)
        search_hotel.search_perform()

        results_title = "Warsaw"
        assert results_title in self.driver.find_element(
            *SearchResultsLocators.search_title).text

    @allure.title("Search hotel test 2")
    @allure.description("This is data driven test of searching hotels")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_hotels_data())
    def test_search_hotel_2(self, data):
        search_hotel = SearchHotelsForm(self.driver)
        search_hotel.open_page()
        search_hotel.set_destination(data.destination)
        search_hotel.set_date_range(data.check_in, data.check_out)
        search_hotel.set_adults_number(data.adults_num)
        search_hotel.set_kids_number(data.kids_num)
        search_hotel.search_perform()

        results_title = data.destination
        assert results_title in self.driver.find_element(
            *SearchResultsLocators.search_title).text
