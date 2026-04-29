# FTV_NKOM_BB_TV_TLF_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and categorizes customer subscriptions for Broadband (BB), TV, and Telephony (TLF) services over historical 6-month periods. It combines monthly aggregated subscription data with dimension information to derive product combinations, detailed product attributes (like speed, technology, dwelling unit type), and counts of each service type per customer/address.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| P3_BB_PRODUCT_KEY |
| P3_BB_PRIM_PRODUCT_KEY |
| P3_TV_PRODUCT_KEY |
| P4_TV_PRODUCT_KEY |
| BB_SUBSCRIPTION_KEY |
| P4_BB_PRODUCT_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| USER_CUSTOMER_KEY |
| SUBSCRIPTION_KEY |
| SUBSCR_FWA_LOC_KEY |
| SUBSCR_USER_LOC_KEY |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| ADDRESS_ID |
| LOCATION_KEY |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUB_PRODUCT_KEY |
| SUBSCRIPTION_KEY |
| SUB_PROD_START_DT_KEY |
| SUB_PROD_END_DT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
| PRODUCT_SPEED |
| TECHNOLOGY |
| VALUECHAIN |
| DWELLING_UNIT_TYPE |
- ← [[DUAL]]

