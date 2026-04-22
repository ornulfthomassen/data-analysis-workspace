# V_TMP_HEH

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed information about active mobile device agreements, their associated products, and customer ownership. It enriches the agreement data by joining it with product master data (for details like reporting levels, categories, and fees) and customer mapping data. It calculates various derived fields such as handset keys, processed IMEI information, product active days, and assigns reporting categories. The `rownum < 3` clause in the provided script suggests that this particular view definition might be intended for testing or temporary purposes, limiting the output to the first two records matching the criteria.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_DEVICE]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

