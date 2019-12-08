class SearchFlightsData:

    def __init__(self, cabin_class, location_from, location_to, start_year, start_month, start_day,
                 end_year, end_month, end_day, adults_num, kids_num, infants_num):
        self.cabin_class = cabin_class
        self.location_from = location_from
        self.location_to = location_to
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day
        self.adults_num = adults_num
        self.kids_num = kids_num
        self.infants_num = infants_num
