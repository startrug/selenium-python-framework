import pytest
import allure

from pages.phptravels.search_flights_form import SearchFlightsForm
from utils.read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestFlightSearch:

    @allure.title("Search flight test")
    @allure.description("This is test of searching flight")
    def test_search_flight_general(self):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        # Trip type: One Way, Round Trip
        search_flight.set_trip_type("Round Trip")
        # Cabin class: Economy, First, Business
        search_flight.set_cabin_class("First")
        search_flight.set_loc_from("LUZ")
        search_flight.set_loc_to("OSL")
        search_flight.set_start_date("2019", "Dec", "25")
        search_flight.set_end_date("2020", "Jun", "2")
        search_flight.set_adults_number(2)
        search_flight.set_kids_number(4)
        search_flight.set_infants_number(1)
        search_flight.search_perform()

    @allure.title("Search flight test: one way")
    @allure.description("This is test of searching one way flight")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_flights_data())
    def test_search_flight_one_way(self, data):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        search_flight.set_one_way()
        search_flight.set_cabin_class(data.cabin_class)
        search_flight.set_loc_from(data.location_from)
        search_flight.set_loc_to(data.location_to)
        search_flight.set_start_date(
            data.start_year, data.start_month, data.start_day)
        search_flight.set_adults_number(data.adults_num)
        search_flight.set_kids_number(data.kids_num)
        search_flight.set_infants_number(data.infants_num)
        search_flight.search_perform()

    @allure.title("Search flight test: round trip")
    @allure.description("This is test of searching round trip flight")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_flights_data())
    def test_search_flight_round_trip(self, data):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        search_flight.set_round_trip()
        search_flight.set_cabin_class(data.cabin_class)
        search_flight.set_loc_from(data.location_from)
        search_flight.set_loc_to(data.location_to)
        search_flight.set_start_date(
            data.start_year, data.start_month, data.start_day)
        search_flight.set_end_date(data.end_year, data.end_month, data.end_day)
        search_flight.set_adults_number(data.adults_num)
        search_flight.set_kids_number(data.kids_num)
        search_flight.set_infants_number(data.infants_num)
        search_flight.get_start_date()
        search_flight.get_end_date()
        search_flight.search_perform()
