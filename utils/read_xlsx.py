import xlrd

from utils.search_flights_data import SearchFlightsData
from utils.search_hotels_data import SearchHotelsData


class XlsxReader:
    @staticmethod
    def get_xlsx_hotels_data():
        wb = xlrd.open_workbook(f"../utils/search_hotels_input_data.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []

        for i in range(1, sheet.nrows):
            search_hotels_data = SearchHotelsData(sheet.cell(i, 0).value,
                                                  sheet.cell(i, 1).value,
                                                  sheet.cell(i, 2).value,
                                                  int(sheet.cell(i, 3).value),
                                                  int(sheet.cell(i, 4).value))
            data.append(search_hotels_data)
        return data

    @staticmethod
    def get_xlsx_flights_data():
        wb = xlrd.open_workbook(f"../utils/search_flights_input_data.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []

        for i in range(1, sheet.nrows):
            search_flights_data = SearchFlightsData(sheet.cell(i, 0).value,  # cabin class
                                                    sheet.cell(i, 1).value,  # trip type
                                                    sheet.cell(i, 2).value,  # location from
                                                    sheet.cell(i, 3).value,  # location to
                                                    int(sheet.cell(i, 4).value),  # start year
                                                    sheet.cell(i, 5).value,  # start month
                                                    int(sheet.cell(i, 6).value),  # start day
                                                    int(sheet.cell(i, 7).value),  # end year
                                                    sheet.cell(i, 8).value,  # end month
                                                    int(sheet.cell(i, 9).value),  # end day
                                                    int(sheet.cell(i, 10).value),  # adults number
                                                    int(sheet.cell(i, 11).value),  # kids number
                                                    int(sheet.cell(i, 12).value))  # infants number
            data.append(search_flights_data)
        return data
