# SCCFED: Smart and Connected Communities Food Environment Dynamics

This repository contains spatial analysis and supporting data files for evaluating **commercially zoned parcels** in Los Angeles County (LAC) and Southern California Association of Governments (SCAG) data, with a focus on supermarket site feasibility.
 
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
| `geojson_viewer.html` | Interactive map to view parcel/CBG overlays |

---

## Methods

- Filtered LAC and SCAG data for **commercial zones**.
- Used CBG shapefiles to compute the **percentage of area** within each CBG covered by those parcels.
- For LAC: also isolated food-related outlets.
- Merged and compared SCAG and LAC outputs for spatial overlap and attribute similarity.

---

## Tools Used

- **Python**: `geopandas`, `shapely`, `numpy`, `pandas`
- **Jupyter Notebooks**
- **Git LFS**: for storing large `.geojson` files
- **HTML**: for visual preview of map overlays

---

## Contact
If you'd like to collaborate or explore this pipeline, reach out via [abigail.horn@usc.edu](mailto:abigail.horn@usc.edu) | [rohitr@usc.edu](mailto:rohitr@usc.edu) 
