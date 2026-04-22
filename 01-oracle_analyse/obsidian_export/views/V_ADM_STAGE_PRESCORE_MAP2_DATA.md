# V_ADM_STAGE_PRESCORE_MAP2_DATA

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates various customer attributes for pre-scoring or analytics purposes. It combines customer demographic data (age), subscription information (such as the number of days a customer has had a specific 'Mobiltelefoni, PostPaid' product and the total number of MPP subscriptions), and customer usage/revenue metrics (like days active, average net revenue over 3 months, and average MB usage over 3 months). The resulting dataset provides a comprehensive profile for each customer (identified by KURT_ID), likely to be used as features in a predictive model or for customer segmentation.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_SCORING_TABLE_CUST]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
- ← [[CLM_CCM.CCM_PRODUCT_DIM_GALAXY_ADJ]]

