# Runner script for all modules
import datetime
from statistics import mean

from energy_info import EnergyData
from house_info import HouseInfo
from humidity_info import HumidityData
from load_data import load_sensor_data
from particle_count_info import ParticleData
from temperature_info import TemperatureData

data = []
print("Welcome to Sensor Data App !!")

# Loads all data from the files in /sensor/datasets
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))

# Retrieves the filtered sensor data from lists. Below are applied filters
# 1) Area = 1
# 2) Date = 5/9/20
houseInfo = HouseInfo(data)
test_area = 1
recs = houseInfo.get_data_by_area("id", rec_area=test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))
test_date = datetime.datetime.strptime("5/9/20", "%m/%d/%y")
recs = houseInfo.get_data_by_date("id", rec_date=test_date)
print("House sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))

# Retrieves the filtered temperature data for the given area/date
# And Finds the Max and Min Temperature for them respectively.
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print("\nHouse Temperature sensor records for area {} = {}".format(test_area, len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))
recs = temperature_data.get_data_by_date(rec_date=test_date)
print("House Temperature sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

# Retrieves the filtered humidity data for the given area/date
# And Finds the Average Humidity for them respectively
humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=test_area)
print("\nHouse Humidity sensor records for area {} = {}".format(test_area, len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))
recs = humidity_data.get_data_by_date(rec_date=test_date)
print("House Humidity sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
print("\tAverrage: {} humidity".format(mean(recs)))

# Retrieves the filtered particulate data for the given area/date
# And Categorizes them based on Air Quality Concentrations respectively.
particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=test_area)
print("\nHouse Particle sensor records for area {} = {}".format(test_area, len(recs)))
concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))
recs = particle_data.get_data_by_date(rec_date=test_date)
print("\nHouse Particle sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

# Retrieves the filtered energy-usage data for the given area/date
# And reports the total energy usages respectively.
energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=test_area)
print("\nHouse Energy sensor records for area {} = {}".format(test_area, len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))
recs = energy_data.get_data_by_date(rec_date=test_date)
print("House Energy sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))
