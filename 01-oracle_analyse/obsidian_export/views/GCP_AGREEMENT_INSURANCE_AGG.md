# GCP_AGREEMENT_INSURANCE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly aggregated summary of specific insurance-related agreement product quantities (opening balance, closing balance, and new contracts). It combines a monthly time series (from January 2020 to the current year, providing the last day of each month) with aggregated data for two categories of products: device insurance, and certain security/personal agreement products. The output includes various descriptive attributes such as product name, group, area, category, and offer name, along with the aggregated quantities for each month and product combination.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.AGREE_PROD_MONTH_FACT_AGG]]
- ← [[GALAXY.AGREEMENT_OFFER_DIM]]
- ← [[GALAXY.AGREEMENT_PRODUCT_DIM_V]]

