import pandas as pd
# from urllib.request import urlretrieve

# medical_data = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

# urlretrieve(medical_data, 'medical.csv')

data = pd.read_csv('medical.csv')

pd.options.display.max_rows = 10

print(data.head())


