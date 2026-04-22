# GCP_STOCK_FTV_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly stock and balance data for Fixed-Line TV (FTV) products. It combines historical monthly balances (both current and previous month's closing balances, up to the last 24 months) with the current month's daily balances (as of end-of-day yesterday). The data is enriched with customer and product dimensions such as age group, customer type, and lifecycle segment. It calculates the beginning balance (UB_MONTH), incoming balance (IB_MONTH), and net balance (NETTO). The primary purpose is to prepare this aggregated and dimensionally enriched dataset for transfer to Google Cloud Platform (GCP).

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_MONTH_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG]]

