import geopandas as gpd
import pandas as pd

# Datasets
estes_park = "data/EstesPark.geojson"
random_points_csv = "data/random_points.csv"
random_points_shapefile = "data/random_points_shapefile/POINT.shp"
random_points_geojson = "data/random_points.geojson"

# Let's turn our Estes Park polygon into a GeoDataFrame
area_of_interest = gpd.read_file(estes_park)

# Now let's take a look at how many points intersect from our geojson file
points_data_geojson = gpd.read_file(random_points_geojson)
intersecting_points = points_data_geojson.overlay(area_of_interest, how='intersection')
print(intersecting_points)

# Looks like five points intersect our polygon! How about the shapefile?
points_data_shapefile = gpd.read_file(random_points_shapefile)
intersecting_points = points_data_shapefile.overlay(area_of_interest, how='intersection')
print(intersecting_points)

# In pandas, you can't just use read_file; you have to be
# more specific about the data type you're reading!
df = pd.read_csv('data/random_points.csv')

# When converting to a DataFrame, you can also set a CRS:
points_data_csv = gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_xy(df['lon'], df['lat']), crs=4326)

# Now that we have a GeoDataFrame, we can run our intersection
intersecting_points = points_data_csv.overlay(area_of_interest, how='intersection')
print(intersecting_points)