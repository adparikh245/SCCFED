import geopandas as gpd
import glob
import os

# List of GeoJSON files to reproject
geojson_files = [
    'la_county_cbgs.geojson',
    'scag_commercial_coverage_by_cbg.geojson',
    'lac_commercial_coverage_by_cbg.geojson',
    'lac_food_coverage_by_cbg.geojson',
]

for file in geojson_files:
    if not os.path.exists(file):
        print(f"File not found: {file}")
        continue
    print(f"Processing {file} ...")
    gdf = gpd.read_file(file)
    # Only reproject if not already in EPSG:4326
    if gdf.crs is None or gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(epsg=4326)
        gdf.to_file(file, driver='GeoJSON')
        print(f"Reprojected and saved: {file}")
    else:
        print(f"Already in EPSG:4326: {file}")
print("\nAll done!")
