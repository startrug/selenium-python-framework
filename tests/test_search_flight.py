import pytest
import allure

from pages.search_flights_form import SearchFlightsForm


@pytest.mark.usefixtures("setup")
class TestFlightSearch:

    @allure.title("Search flight test")
    @allure.description("This is test of searching Flight from Swidnik to Oslo")
    def test_search_flight(self):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        search_flight.set_one_way()
        search_flight.set_first_class()
        search_flight.set_adults_number(2)
        search_flight.set_kids_number(4)
        search_flight.set_infants_number(1)
        search_flight.search_perform()
