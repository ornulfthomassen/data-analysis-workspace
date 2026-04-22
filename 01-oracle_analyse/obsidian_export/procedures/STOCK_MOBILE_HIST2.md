# STOCK_MOBILE_HIST2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates and stores daily mobile subscription stock data, enriching it with product and discount information. The procedure extracts raw subscription data for a specific day, processes it through several intermediate stages to identify main products and applied discounts, and finally consolidates this information into a detailed daily stock table and a summarized aggregated table.

## Data Sources (Inputs)
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_DISCOUNT_PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_PROFIT_CAT_SUBS_HIST]]

## Target Tables (Outputs)
- → [[TMP_STOCK_MOBILE_HIS2_CM]]
- → [[TMP_STOCK_MOBILE_HIST2_RAW]]
- → [[STOCK_MOBILE_HIST2_DET]]
- → [[TMP_STOCK_MOBILE_HIST2_AGG_SUB]]
- → [[STOCK_MOBILE_HIST2_AGG]]

