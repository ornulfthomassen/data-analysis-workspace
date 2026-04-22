# GCP_TELENORBUTIKKEN_CUST_COUNTER

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares anonymized Telenorbutikken sales or event details for loading into Google Cloud Platform (GCP). It combines raw event/sales data from a staging table with dealer dimension information, enriching details like dealer name and group, and filters records to include only those from the last three years.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MAZE_STAGE]]
- ← [[GALAXY.DEALER_DIM]]

