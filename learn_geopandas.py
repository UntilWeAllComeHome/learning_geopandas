import geopandas as gpd

# Datasets
estes_park = "data/EstesPark.geojson"
random_points_csv = "data/random_points.csv"
random_points_shapefile = "data/random_points_shapefile/POINT.shp"
random_points_geojson = "data/random_points.geojson"

points = [random_points_csv, random_points_shapefile, random_points_geojson]

# Geopandas can handle a wide range of datatypes. In
# this demo, we'll use a Shapefile, geojson, and a CSV.
# For our scenario, we're interested in which points 
# intersect our polygon.

area_of_interest = gpd.read_file(estes_park)

intersections = []

for dataset in points:
    points_data = gpd.read_file(dataset)
    intersecting_points = area_of_interest.geometry.intersects(points_data.geometry)
    intersections.append(intersecting_points)

print(intersections)