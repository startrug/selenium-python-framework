import pytest
import allure

from pages.phptravels.search_tours_form import SearchToursForm
from utils.read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestTourSearch:

    @allure.title("Search tours test")
    @allure.description("This is test of searching tour")
    def test_search_tour_general(self):
        search_tour = SearchToursForm(self.driver)
        search_tour.open_page()
        search_tour.open_tours_tab()
        search_tour.set_tour_destination("Sheraton Trip")
        search_tour.set_tour_type("Private")
        search_tour.set_date("2020", "Jan", "3")
        search_tour.set_adults_number(10)
        search_tour.search_perform()

    @allure.title("Search flight test: one way")
    @allure.description("This is test of searching one way flight")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_tours_data())
    def test_search_tour_data_driven(self, data):
        search_tour = SearchToursForm(self.driver)
        search_tour.open_page()
        search_tour.open_tours_tab()
        search_tour.set_tour_destination(data.destination)
        search_tour.set_tour_type(data.tour_type)
        search_tour.set_date(data.start_year, data.start_month, data.start_day)
        search_tour.set_adults_number(data.adults_num)
        search_tour.search_perform()
