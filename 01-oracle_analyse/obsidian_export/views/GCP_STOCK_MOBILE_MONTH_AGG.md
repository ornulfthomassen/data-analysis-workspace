# GCP_STOCK_MOBILE_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates mobile subscription stock data on a monthly basis, combining historical monthly data with daily data for the current month. It calculates 'Unbilled' (UB_MONTH), 'Invoiced' (IB_MONTH), and 'Netto' (UB_MONTH - IB_MONTH) balances, along with aggregated discounts. The data is enriched with various dimensions such as product categories, customer lifecycle segments, and owner/user age groups. The view primarily serves to prepare and stage data for transfer to Google Cloud Platform (GCP), providing data from approximately the last two years.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_MONTH_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]

