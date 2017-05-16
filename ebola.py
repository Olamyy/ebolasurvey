import numpy
import pandas
import csv
from pprint import pprint
from matplotlib import pyplot

working_dictionary = {}

unpacking = pandas.read_excel('/home/terragon/Downloads/ebola_data_db_format.xlsx', parse_rows=['A'])

pprint(unpacking)