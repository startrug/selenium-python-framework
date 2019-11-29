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
        search_flight.set_cabin_class("First")  # Cabin class: Economy, First, Business
        search_flight.set_loc_from("LUZ")
        search_flight.set_loc_to("OSL")
        search_flight.set_start_month("Dec")  # month: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
        search_flight.set_start_day("30")
        search_flight.set_adults_number(2)
        search_flight.set_kids_number(4)
        search_flight.set_infants_number(1)
        search_flight.search_perform()
