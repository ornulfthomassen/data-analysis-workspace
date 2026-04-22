# CI_CUST_CONTACT_HISTORY_FULL

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates customer contact history data from three separate source tables into a single, unified dataset. It combines records from CI_CUST_CONTACT_HISTORY_3_FIX, CI_CUST_CONTACT_HISTORY2_FIX, and CI_CUST_CONTACT_HISTORY_1_FIX using UNION ALL, ensuring that all customer contact history, potentially from different periods or partitions, is available through one consistent interface. Minor data type casting is performed to harmonize column types across the merged datasets.

## Data Sources (Inputs)
- ← [[clm_kim.CI_CUST_CONTACT_HISTORY_3_FIX]]
- ← [[clm_kim.CI_CUST_CONTACT_HISTORY2_FIX]]
- ← [[clm_kim.CI_CUST_CONTACT_HISTORY_1_FIX]]

