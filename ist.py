import warnings
warnings.filterwarnings('ignore')

import pandas as pd

airbnb_data = pd.read_csv('NYC_airbnb.csv')


user_nbhd = input('Choose from Manhattan, Brooklyn, Queens, Bronx, Staten Island: ')
user_nhhd_result = airbnb_data[airbnb_data['neighbourhood_group'] == user_nbhd]
print(user_nhhd_result.sample(2))
