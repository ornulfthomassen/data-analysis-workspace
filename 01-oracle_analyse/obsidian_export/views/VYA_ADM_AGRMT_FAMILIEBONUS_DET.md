# VYA_ADM_AGRMT_FAMILIEBONUS_DET

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and presents detailed family bonus agreement data on a monthly basis. It combines agreement, customer, and product information to identify customer owners and members, determine unit types (like swap agreements or subscriptions), and calculate bonus eligibility (REWARD). The view also provides product-specific attributes and counts of various subscription types owned or used by customers, primarily for reporting and data loading purposes (e.g., to MJØSA).

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
| AGREEMENT_ID |
| SRC_AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| ROOT_PRODUCT_OFFER_ID |
| PRODUCT_OFFER_ID |
| SRC_ROOT_PRODUCT_ID |
| SRC_PRODUCT_ID |
| ORIGINAL_START_DATE |
| END_DATE |
| START_DATE |
| CUSTOMER_ID_OWNER |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
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
| SWAP_AGREEMENT_OFFER_ID |
| FIXEDBROADBAND_SUBSCRIPTION_ID |
| CUSTOMER_ROLE |
| POID |
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
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
| PERIOD_MONTH_KEY |
| MOB_SUBSCR_ID |
| CUSTOMER_SK |
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_GROUP_CLM |
| PRODUCT_AREA |
| PRODUCT_CATEGORY |
| PRODUCT_REPORTING |
| PRODUCT_PAYMENT |
| PRODUCT_FAMILY_NAME |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]
| Column Name |
|---|
| SRC_AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |
| ORIGINAL_START_DATE |

