import datetime;

'''
The below extendable class filters the datalist based on area/date
on any applied field (eg. ID)
'''


class HouseInfo:
    def __init__(self, data):
        self.data = data

    '''
    The below method returns filtered data based on the supplied field and area.
    @:param field:
    @:param rec_area:
    @:return field_data
    '''

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
                record[field] = field_data
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    '''
    The below method returns filtered data based on the supplied field and date.
    @:param field:
    @:param rec_date:
    @:return field_data
    '''

    def get_data_by_date(self, field, rec_date=datetime.date.today()):
        field_data = []
        for record in self.data:
            if record['date'] == rec_date.strftime("%m/%d/%y"):
                field_data.append(record[field])
        return field_data
