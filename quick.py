import geopandas as gpd
import pandas as pd

# Datasets
estes_park = "data/EstesPark.geojson"
random_points_csv = "data/random_points.csv"
random_points_shapefile = "data/random_points_shapefile/POINT.shp"
random_points_geojson = "data/random_points.geojson"

area_of_interest = gpd.read_file(estes_park)
area_of_interest["city"] = "Estes Park"

df = pd.read_csv('data/random_points.csv')
points_data= gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_xy(df['lon'], df['lat']), crs=4326)

intersecting_points = points_data.overlay(area_of_interest, how='intersection')
print(intersecting_points)