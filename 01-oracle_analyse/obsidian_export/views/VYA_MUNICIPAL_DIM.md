# VYA_MUNICIPAL_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated dimension for Norwegian municipal, sub-county, county, and region data. It combines current (historically valid until '9999-12-31') and historical records, specifically addressing municipality code changes by linking old records to their current municipal counterparts. The view standardizes data types and formats for all fields, making it suitable for analytical consumption, likely in a data warehousing or business intelligence environment (e.g., Viya).

## Data Sources (Inputs)
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]

