# LIGHT_AGREEMENT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "LIGHT_AGREEMENT_V", provides a comprehensive, denormalized, and categorized dataset focused on customer agreements. It consolidates details from various sources to offer a holistic view encompassing agreement specifics, associated products and services, customer and household demographics, subscription metrics (including mobile broadband usage), handset information, and sales channel data. The view enriches the raw data by classifying products into families (e.g., PostPaid, SWAP, DSL), grouping mobile broadband usage, and flagging various security/safety service subscriptions and their activation statuses. It appears to be designed for analytical reporting or further data consumption within a CRM or customer intelligence system.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_AGREEMENT]]
- ← [[CLM_CCM.CCM_AGREEMENT_MEMBER]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
- ← [[CLM_CCM.CCM_AGREEMENT_MEMBER_PIVOT_V]]
- ← [[clm_ccm.V_CCM_AGRM_SFTY_USE]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
- ← [[GALAXY.HANDSET_DIM_V]]

