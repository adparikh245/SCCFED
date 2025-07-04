# SCCFED: Commercial Coverage Analysis for Food Equity Planning

This repository contains spatial analysis and supporting data files for evaluating **commercially zoned parcels** in Los Angeles County (LAC) and Southern California Association of Governments (SCAG) data, with a focus on supermarket site feasibility.

It supports the study:

> **"Equitable Facility Location for Supermarket Interventions with Large-Scale Mobility Data"**  
---

## Project Goal

To determine the **proportion of each Census Block Group (CBG)** that is covered by commercially zoned parcels, and to conduct a comparative analysis across zoning datasets from:

-  **SCAG** (Southern California Association of Governments)
-  **LAC Assessor’s Office** (Los Angeles County)

This is the first step in identifying feasible locations for future supermarkets, in line with optimization models from the main paper.

---

## What This Repo Contains

| File | Description |
|------|-------------|
| `scag_commercial_parcels.geojson` | GeoJSON of SCAG commercial parcels |
| `lac_commercial_parcels_sample.geojson` | Sample of LAC commercial parcels |
| `scag_commercial_coverage_by_cbg.geojson` | Proportion of each CBG covered by SCAG parcels |
| `lac_food_coverage_by_cbg.geojson` | CBG-level food outlet coverage (LAC data) |
| `lac_commercial_coverage_by_cbg.geojson` | CBG-level commercial coverage (LAC data) |
| `la_county_cbgs.geojson` | CBG boundaries used for analysis |
| `analysis.ipynb` | Notebook containing all calculations and visuals |
| `geojson_viewer.html` | Interactive map to view parcel/CBG overlays |

---

## Methods

- Filtered LAC and SCAG data for **commercial zones** (use codes starting with 1 or 2).
- Used CBG shapefiles to compute the **percentage of area** within each CBG covered by those parcels.
- For LAC: also isolated **food-related outlets** (use codes like 14–16, 21, 131, etc.).
- Merged and compared SCAG and LAC outputs for spatial overlap and attribute similarity.

---

## Tools Used

- **Python**: `geopandas`, `shapely`, `matplotlib`, `osmnx`
- **Jupyter Notebooks**
- **Git LFS**: for storing large `.geojson` files
- **HTML**: for standalone visual preview of map overlays
- Optional: QGIS or ArcGIS for deeper cartographic editing

---

## Next Steps

- Integrate these coverage metrics with zoning constraints in the LSCP/MCLP models.
- Overlay food coverage with supermarket accessibility gaps.
- Align with DRP land-use restrictions to evaluate realistic intervention sites.

---

## 📬 Contact
If you'd like to collaborate or explore this pipeline, reach out via [rohitr@usc.edu](mailto:rohitr@usc.edu) or [abigail.horn@usc.edu](mailto:abigail.horn@usc.edu).

