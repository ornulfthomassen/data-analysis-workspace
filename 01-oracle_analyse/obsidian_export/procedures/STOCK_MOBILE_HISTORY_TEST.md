# STOCK_MOBILE_HISTORY_TEST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The script processes daily subscription and product data, calculates associated discounts, and aggregates this information into several temporary staging tables. It enriches subscription data with customer demographics (age, lifecycle segments) and product attributes. The final aggregation calculates subscription balances and total discounts, likely for reporting or further analytical processing. The procedure also logs its execution history using `CRM_ANALYSE.P_ADM_LOAD_HISTORY` at various stages.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.ACCOUNT_CUSTOMER_MAP]]
- ← [[CCDW.CUSTOMER_PROFILE_KURT]]
- ← [[CCDW.CLM_LIVSFASE_SEGMENT]]
- ← [[CCDW.PRODUCT_PROFIT_SEGMENT]]
- ← [[CCDW.PRODUCT_ATTRIBUTE_PER_PERIOD]]
- ← [[CCDW.DISCOUNT_PRODUCT_DEFINITION]]
- ← [[V_TABLE_TMP]]

## Target Tables (Outputs)
- → [[V_TABLE_RAW]]
- → [[V_TABLE_DET]]
- → [[V_TABLE_AGG]]

