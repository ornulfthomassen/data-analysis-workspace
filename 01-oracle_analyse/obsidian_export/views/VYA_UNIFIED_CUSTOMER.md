# VYA_UNIFIED_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a unified, aggregated profile of enterprise/company ('FORETAK') customers, including their product subscriptions (mobile telephony, fixed internet, TV, mobile internet, fixed telephony, mobile IoT), various service counts (e.g., number of mobile lines, data bonuses, swap programs), household-level service aggregations, and core business information (organization number, address, employee count, credit profile, service concept, company type, segment) for reporting and analytical purposes. It also categorizes customers based on their classification for reporting purposes.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.CUSTOMER_DIM_MV]]
- ← [[ODS.CUSTOMER_ODS]]
- ← [[GALAXY.CUSTOMER_RELATION_PROFILE_FACT]]
- ← [[GALAXY.COUNTERPART_DIM]]

