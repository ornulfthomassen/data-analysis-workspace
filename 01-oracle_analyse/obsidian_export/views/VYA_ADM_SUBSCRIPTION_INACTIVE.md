# VYA_ADM_SUBSCRIPTION_INACTIVE

**Schema:** `CCM` | **Type:** `View`

## Description
This view generates a comprehensive monthly historical snapshot of telecommunication subscriptions. It aggregates and enriches data from various historical tables to provide detailed information on subscription characteristics, associated customer profiles, product attributes, device usage, market area, porting history, and aggregated usage statistics (data, MMS, SMS, voice) and revenue metrics over the past three months. The primary purpose is to create a rich dataset for analytical purposes, such as customer lifecycle analysis, churn prediction, or segment profiling, despite the 'INACTIVE' in its name not being explicitly filtered in the SQL.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[CRM_ANALYSE.ADM_MARKET_AREA_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG_I]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[CLM_ADM.ADM_MOBIL_PORT_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST_I]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

