import datetime

from house_info import HouseInfo


class ParticleData(HouseInfo):

    def __init__(self, data):
        super().__init__(data)

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("particulate", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=datetime.date.today()):
        recs = super().get_data_by_date("particulate", rec_date)
        return self._convert_data(recs)

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs

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
