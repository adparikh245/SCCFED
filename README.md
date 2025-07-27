# SCCFED: Smart and Connected Communities Food Environment Dynamics

This repository contains spatial analysis and supporting data files for evaluating **commercially zoned parcels** in Los Angeles County (LAC) and Southern California Association of Governments (SCAG) data, with a focus on supermarket site feasibility.

> **About the Data Sources**  
> - **SCAG** (Southern California Association of Governments) is the nation’s largest metropolitan planning organization, covering six counties in Southern California. It provides regionally harmonized zoning and land-use datasets used for infrastructure and development planning.  
> - **LAC** (Los Angeles County) maintains its own high-resolution, parcel-level zoning and land use data. This dataset offers more detailed classifications specific to L.A. County’s jurisdiction.

---

## Project Goal

To determine the **proportion of each Census Block Group (CBG)** that is covered by commercially zoned parcels, and to conduct a comparative analysis across zoning datasets from:

-  **SCAG** (Southern California Association of Governments)
-  **LAC** (Los Angeles County)

This identifies feasible locations for future supermarkets, in line with optimization models from the main paper.

---

## What This Repo Contains

| File | Description |
|------|-------------|
| `scag_commercial_parcels.json` | GeoJSON of SCAG commercial parcels |
| `lac_commercial_parcels_sample.json` | Sample of LAC commercial parcels |
| `scag_commercial_coverage_by_cbg.json` | Proportion of each CBG covered by SCAG parcels |
| `lac_food_coverage_by_cbg.json` | CBG-level food outlet coverage (LAC data) |
| `lac_commercial_coverage_by_cbg.json` | CBG-level commercial coverage (LAC data) |
| `la_county_cbgs.json` | CBG boundaries used for analysis |
| `analysis.ipynb` | Notebook containing all calculations and visuals |
| `index.html` | Interactive map to view parcel/CBG overlays |
| `cbg_parcel_coverage_summary.xlsx` | formatted data analysis for coverage % |

---

## Methods

- Filtered LAC and SCAG data for **commercial zones**.
- Used CBG shapefiles to compute the **percentage of area** within each CBG covered by those parcels.
- For LAC: also isolated food-related outlets.
- Merged and compared SCAG and LAC outputs for spatial overlap and attribute similarity.
- FULL REPORT for **more info on methodology + detailed review of repo:** [Report Link](https://docs.google.com/document/d/1hlX9L6iqkRNPcUR1n-hzSdv-3MY1HdgH5r_m41ML1aE/edit)
---

## Tools Used

- **Python**: `geopandas`, `shapely`, `numpy`, `pandas`
- **Jupyter Notebooks**
- **Git LFS**: for storing large `.geojson` files
- **HTML**: for visual preview of map overlays

---
## Data Sets:
- LAC (2019): https://data.lacounty.gov/documents/lacounty::parcels/about
- SCAG (2019): https://hub.scag.ca.gov/datasets/3e9c888c6aae45ab8e140abeec42cd1e_0/about
- CBG (2024): https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2024&layergroup=Block+Groups

---

## Contact
If you'd like to collaborate or explore this pipeline, reach out via [abigail.horn@usc.edu](mailto:abigail.horn@usc.edu) | [rohitr@usc.edu](mailto:rohitr@usc.edu) 
