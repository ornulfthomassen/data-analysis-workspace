# HOUSEHOLD_LAT_LONG_SHOP_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed household demographic and address information with geographical coordinates (latitude and longitude) and calculated distances to specific shops or dealers. It applies data quality checks to latitude and longitude values, setting them to NULL if invalid. Additionally, it appends two placeholder rows (with HOUSEHOLD_ID -1 and -2) to represent 'unknown' or 'generic' household entries, providing default values for all fields, which can be useful for reporting or analytical purposes where a default category is required.

## Data Sources (Inputs)
- ← [[CLM_ccm.CCM_HOUSEHOLD_INFO]]
- ← [[FARID_SHOP_DISTANCE]]

