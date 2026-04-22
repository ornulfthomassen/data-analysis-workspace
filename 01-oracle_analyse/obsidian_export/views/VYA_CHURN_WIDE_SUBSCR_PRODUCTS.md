# VYA_CHURN_WIDE_SUBSCR_PRODUCTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly, wide-format dataset of active postpaid voice subscription products for specific market areas (2 and 4). It joins subscription details with associated product information (both primary and sub-product details) for each month. The data is filtered to include only products active within a given month and covers approximately the last two years of data relative to the current month. Its primary purpose, as suggested by 'CHURN' in its name, is likely to serve as a consolidated data source for analyzing customer churn related to specific subscription products and their attributes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]

