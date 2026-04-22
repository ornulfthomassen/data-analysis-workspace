# VYA_AGREEMENT_INSURANCE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides an aggregated, monthly overview of agreement product quantities (opening balance, closing balance, new customers) for specific insurance and security-related products. It combines monthly date dimension data with detailed agreement product and offer information, categorizing products by group, area, and market product type, focusing on 'Device Insurance' and 'Security/Agreement Products'. It includes filters to exclude certain product types and test data for specific periods.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.AGREE_PROD_MONTH_FACT_AGG]]
- ← [[GALAXY.AGREEMENT_OFFER_DIM]]
- ← [[GALAXY.AGREEMENT_PRODUCT_DIM_V]]

