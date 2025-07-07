import geopandas as gpd
import pandas as pd

# Load coverage GeoJSONs
scag_gdf = gpd.read_file('scag_commercial_coverage_by_cbg.geojson')
lac_com_gdf = gpd.read_file('lac_commercial_coverage_by_cbg.geojson')
lac_food_gdf = gpd.read_file('lac_food_coverage_by_cbg.geojson')

# Extract only the key columns
scag_df     = pd.DataFrame(scag_gdf[['GEOID','covered_area']]).rename(columns={'covered_area':'scag_area'})
lac_com_df  = pd.DataFrame(lac_com_gdf[['GEOID','covered_area']]).rename(columns={'covered_area':'lac_com_area'})
lac_food_df = pd.DataFrame(lac_food_gdf[['GEOID','covered_area']]).rename(columns={'covered_area':'lac_food_area'})

# Merge on GEOID
combined = (
    scag_df
    .merge(lac_com_df,  on='GEOID', how='outer')
    .merge(lac_food_df, on='GEOID', how='outer')
    .fillna(0)
)

# Load CBG areas from the current CBG file
cbg_gdf = gpd.read_file('la_county_cbgs.geojson').to_crs('EPSG:3310')
cbg_gdf['cbg_area'] = cbg_gdf.geometry.area
cbg_areas = cbg_gdf[['GEOID', 'cbg_area']]

# Merge areas
combined = combined.merge(cbg_areas, on='GEOID', how='left')

# Add total covered area and coverage percentage
combined['total_area_covered'] = (
    combined['scag_area']
  + combined['lac_com_area']
  + combined['lac_food_area']
)
combined['coverage_pct'] = (combined['total_area_covered'] / combined['cbg_area'] * 100).round(2)

# Export to CSV
combined.to_csv('cbg_parcel_coverage_summary.csv', index=False)
print('Written ➔ cbg_parcel_coverage_summary.csv') 