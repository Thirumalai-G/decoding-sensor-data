import datetime

from house_info import HouseInfo

'''
The below class filters the datalist based on area/date
on Particulate Field by extending HouseInfo
'''


class ParticleData(HouseInfo):

    def __init__(self, data):
        super().__init__(data)

    '''
    The below method returns filtered data based on the particulate and area.
    @:param rec_area:
    @:return field_data
    '''

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("particulate", rec_area)
        return self._convert_data(recs)

    '''
      The below method returns filtered data based on the particulate and date.
      @:param rec_date:
      @:return field_data
      '''

    def get_data_by_date(self, rec_date=datetime.date.today()):
        recs = super().get_data_by_date("particulate", rec_date)
        return self._convert_data(recs)

    '''
     The below util method converts particulate list from string to float
     @:param data:
     @:return recs
     '''

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs

    '''
     The below method maps every data record based on the particulate content as 
     Good, Moderate, Bad and returns the grouped collection.
     @:param data:
     @:return particulate
     '''

    def get_data_concentrations(self, data):
        particulate = {"good": 0, "moderate": 0, "bad": 0}
        for rec in data:
            if rec <= 50.0:
                particulate['good'] += 1
            elif rec > 100.0:
                particulate['bad'] += 1
            else:
                particulate['moderate'] += 1
        return particulate
