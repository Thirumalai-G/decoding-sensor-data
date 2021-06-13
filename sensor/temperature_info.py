import datetime

from house_info import HouseInfo

'''
The below class filters the data-list based on area/date
on Temperature Field by extending HouseInfo
'''


class TemperatureData(HouseInfo):

    def __init__(self, data):
        super().__init__(data)

    '''
    The below method returns filtered data based on the temperature and area.
    @:param rec_area:
    @:return field_data
    '''

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("temperature", rec_area)
        return self._convert_data(recs)

    '''
    The below method returns filtered data based on the temperature and date.
    @:param rec_date:
    @:return field_data
    '''

    def get_data_by_date(self, rec_date=datetime.date.today()):
        recs = super().get_data_by_date("temperature", rec_date)
        return self._convert_data(recs)

    '''
    The below util method converts temperature list from string to int-base10
    @:param data:
    @:return recs
    '''

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(int(rec, base=10))
        return recs
