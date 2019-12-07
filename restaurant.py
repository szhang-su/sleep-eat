import warnings
warnings.filterwarnings('ignore')

import pandas as pd
restaurants = pd.read_csv('NYC_Restaurants.csv')
print(restaurants.sample(5))

food = restaurants[(restaurants['BORO'] == 'MANHATTON') & (restaurants['CUSINE DESCRIPTION'] == 'Mexican')]
food['BORO'].value_count()