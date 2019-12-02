import xlrd
from utils.search_hotels_data import SearchHotelsData


class XlsxReader:
    @staticmethod
    def get_xlsx_data():
        wb = xlrd.open_workbook(f"../utils/search_hotels_input_data.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []

        for i in range(1, sheet.nrows):
            search_hotels_data = SearchHotelsData(sheet.cell(i, 0).value, sheet.cell(i, 1).value,
                                                  sheet.cell(i, 2).value, int(sheet.cell(i, 3).value),
                                                  int(sheet.cell(i, 4).value))
            data.append(search_hotels_data)
        return data

