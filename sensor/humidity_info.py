import datetime

from house_info import HouseInfo

'''
The below class filters the datalist based on area/date
on Humidity Field by extending HouseInfo
'''


class HumidityData(HouseInfo):

    def __init__(self, data):
        super().__init__(data)

    '''
    The below method returns filtered data based on the humidity and area.
    @:param rec_area:
    @:return field_data
    '''

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("humidity", rec_area)
        return self._convert_data(recs)

    '''
    The below method returns filtered data based on the humidity and date.
    @:param rec_date:
    @:return field_data
    '''

    def get_data_by_date(self, rec_date=datetime.date.today()):
        recs = super().get_data_by_date("humidity", rec_date)
        return self._convert_data(recs)

    '''
    The below util method converts humidity list from string to percentage
    @:param data:
    @:return recs
    '''

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec) * 100)
        return recs
