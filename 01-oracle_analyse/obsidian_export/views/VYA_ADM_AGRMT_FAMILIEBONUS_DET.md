# VYA_ADM_AGRMT_FAMILIEBONUS_DET

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a monthly detailed view of customer agreements related to 'family bonus' programs, including information about the owner and member customers, associated products, and counts of various subscription types that contribute to a 'reward' calculation. It captures a snapshot of these details for each month.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[ODS.AGREEMENT_ODS_MOB]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[ODS.AGREEMENT_MEMBER_CUSTOMER_MOB]]
- ← [[CLM_ADM.ADM_FB_ACCESSES_CUST_HIST]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]

