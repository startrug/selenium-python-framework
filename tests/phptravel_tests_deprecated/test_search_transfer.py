import pytest
import allure

from pages.phptravels.search_transfers_form import SearchTransfersForm
from utils.read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestTransferSearch:

    @allure.title("Search transfers test")
    @allure.description("This is test of searching transfers")
    def test_search_transfer_general(self):
        search_transfer = SearchTransfersForm(self.driver)
        search_transfer.open_page()
        search_transfer.open_transfer_tab()
        search_transfer.set_pick_up_loc("Manchester")
        search_transfer.set_drop_off_loc("Petra")
        search_transfer.set_depart_date("2019", "Dec", "29")
        search_transfer.set_depart_time("12:30")
        search_transfer.set_return_date("2020", "Jan", "8")
        search_transfer.set_return_time("15:00")
        search_transfer.search_perform()

    @allure.title("Search transfer test")
    @allure.description("This is test of searching transfer")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_transfers_data())
    def test_search_transfer_data_driven(self, data):
        search_transfer = SearchTransfersForm(self.driver)
        search_transfer.open_page()
        search_transfer.open_transfer_tab()
        search_transfer.set_pick_up_loc(data.pick_up_loc)
        search_transfer.set_drop_off_loc(data.drop_off_loc)
        search_transfer.set_depart_date(
            data.depart_year, data.depart_month, data.depart_day)
        search_transfer.set_depart_time(data.depart_time)
        search_transfer.set_return_date(
            data.return_year, data.return_month, data.return_day)
        search_transfer.set_return_time(data.return_time)
        search_transfer.search_perform()
