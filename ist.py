import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

# Read data from csv
airbnb_data_origin= pd.read_csv('NYC_airbnb.csv')
airbnb_data = airbnb_data_origin.filter(['neighbourhood_group', 'price', 'room_type', 'number_of_reviews', 'latitude',
                                         'longitude', 'name', 'host_id'])

# Filter by neighborhood
user_nbhd = input('Choose from Manhattan, Brooklyn, Queens, Bronx, Staten Island: ')
user_nbhd_result = airbnb_data[airbnb_data['neighbourhood_group'] == user_nbhd]

# Filter by room type
user_room = input(f"Choose from 'Private room', 'Entire home/apt', 'Shared room'")
user_room_result = user_nbhd_result[user_nbhd_result['room_type'] == user_room]

# Filter by price group
user_room_result['price_group'] = np.nan
user_room_result['price_group'][user_room_result['price'] <= 50] ='0-50'
user_room_result['price_group'][user_room_result['price'].between(51, 101)] = '51-100'
user_room_result['price_group'][user_room_result['price'].between(101, 151)] = '101-150'
user_room_result['price_group'][user_room_result['price'].between(151, 201)] = '151-200'
user_room_result['price_group'][user_room_result['price'] > 200] ='200-'
user_price = input(f"Choose price range from '0-50', '51-100', '101-150','151-200' and '200-'")
user_price_result = user_room_result[user_room_result['price_group'] == user_price]
# Sort the rooms by number of reviews from high to low
final_sort = user_price_result.sort_values(by=['number_of_reviews'], ascending=False)
print(final_sort.head(10))

import folium
from IPython.display import display

CENTER_NYC = (40.7128, -74.0060)
map = folium.Map(location=CENTER_NYC, zoom_start=12)

for row in final_sort.to_records():
    pos = (row['latitude'], row['longitude'])
    marker = folium.Marker(location=pos, popup="%s" % (row['name'])
                          )
    map.add_child(marker)
display(map)