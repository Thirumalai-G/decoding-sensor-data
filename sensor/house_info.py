import datetime;


class HouseInfo:
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
                record[field] = field_data
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date=datetime.date.today()):
        field_data = []
        for record in self.data:
            if record['date'] == rec_date.strftime("%m/%d/%y"):
                field_data.append(record[field])
        return field_data
