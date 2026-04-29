# VYA_ADM_AGRMT_FAMILIEBONUS_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates customer agreement data, specifically related to 'Familiebonus' (Family Bonus) products, by month, customer, and agreement. It calculates the number of members in an agreement, reward units, and sums various types of subscriptions owned or used (postpaid, mobile broadband, fixed broadband, telephony, fiber, coax, TV, IP phone). The purpose is to load customer data to 'Mjøsa' (likely a data warehouse or reporting system).

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
| LAST_DATE |
- ← [[ODS.AGREEMENT_ODS_MOB]]
| Column Name |
|---|
| START_DATE |
| END_DATE |
| SRC_ROOT_PRODUCT_ID |
| CUSTOMER_ID_OWNER |
| AGREEMENT_ID |
| SRC_AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| ROOT_PRODUCT_OFFER_ID |
| PRODUCT_OFFER_ID |
| SRC_PRODUCT_ID |
| ORIGINAL_START_DATE |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[ODS.AGREEMENT_MEMBER_CUSTOMER_MOB]]
| Column Name |
|---|
| SRC_AGREEMENT_ID |
| START_DATE |
| END_DATE |
| CUSTOMER_ID |
- ← [[CLM_ADM.ADM_FB_ACCESSES_CUST_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| NUM_PRIV_POSTPAID_SUBS_OWNED |
| NUM_BUS_POSTPAID_SUBS_USED |
| NUM_SWAP_AGREEMENTS_OWNED |
| NUM_MBB_SUBS_OWNED |
| NUM_FIXED_BROADBAND_OWNED |
| NUM_FIXED_TELEPHONY_SUBS_OWNED |
| NUM_FIBER_CDK |
| NUM_COAX_CDK |
| NUM_TV_CDK |
| NUM_IP_PHONE_CDK |
| MOB_SUBSCR_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]
| Column Name |
|---|
| SRC_AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| SRC_PRODUCT_ID |
| START_DATE |
| END_DATE |

