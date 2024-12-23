import folium
from pyproj import crs
import geopandas as gpd
import matplotlib.pyplot as plt

# Create a Map instance
m = folium.Map(location=[60.25, 24.8], zoom_start=10, control_scale=True)

m

outfp = "CS-257-Final-Project/flaskApp_test/templates/base_map.html"
m.save(outfp)
