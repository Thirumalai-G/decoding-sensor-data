import datetime

from house_info import HouseInfo

'''
The below class filters the datalist based on area/date
on EnergyUsage Field by extending HouseInfo
'''


class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    def __init__(self, data):
        super().__init__(data)

    '''
    The below method returns filtered data based on the energy_usage and area.
    @:param rec_area:
    @:return field_data
    '''

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    '''
    The below method returns filtered data based on the energy_usage and date.
    @:param rec_date:
    @:return field_data
    '''

    def get_data_by_date(self, rec_date=datetime.date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    '''
    The below Util Methods (_get_energy,_convert_data) converts energy usage 
    from hexadecimal to numeric
    '''

    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy * self.ENERGY_BITS
        energy = energy >> 4
        return energy

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    '''
    The below method calculates total energy usage provided energy consumed per
    bulb. 
    '''

    def calculate_energy_usage(self, data):
        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
        return total_energy
