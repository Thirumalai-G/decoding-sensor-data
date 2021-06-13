import csv
import glob
import os

'''
Loads Data Files from the /datasets directory
Reads all the data into a list.
:@returns sensor_data
'''


def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    for sensor_file in sensor_files:
        with open(sensor_file, 'r') as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data
