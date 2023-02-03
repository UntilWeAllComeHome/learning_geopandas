import geopandas as gpd

# Datasets
estes_park = "data/EstesPark.geojson"
random_points_csv = "data/random_points.csv"
random_points_shapefile = "data/random_points_shapefile/POINT.shp"
random_points_geojson = "data/random_points.geojson"

area_of_interest = gpd.read_file(estes_park)

# Let's take a look at how many points intersect from our geojson file
points_data = gpd.read_file(random_points_geojson)
intersecting_points = points_data.overlay(area_of_interest, how='intersection')
print(intersecting_points)

# Looks like five points intersect our polygon! How about the shapefile?
points_data = gpd.read_file(random_points_shapefile)
intersecting_points = points_data.overlay(area_of_interest, how='intersection')
print(intersecting_points)

# Same thing! Which makes sense becaue they are the exact same dataset.

# What about the CSV?
points_data = gpd.read_file(random_points_csv)
intersecting_points = points_data.overlay(area_of_interest, how='intersection')
print(intersecting_points)