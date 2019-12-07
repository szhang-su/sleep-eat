! pip install folium
import folium
import pandas as pd
import random
CENTER_NYC = (40.7128,-74.0060)
map = folium.Map(location=CENTER_NYC, zoom_start=12)
map
for row in data.to_records():
    pos = (row['latitude'],row['longitude'])
    marker = folium.Marker(location=pos,
                    popup="%s, %s" % (row['name'],row['neighbourhood_ground'])
                          )
    map.add_child(marker)
