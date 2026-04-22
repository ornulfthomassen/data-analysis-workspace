# VYA_ADM_AGRMT_FAMILIEBONUS_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly customer and agreement-related data, specifically focusing on 'Familiebonus' (Family Bonus) agreements. It calculates various metrics such as the number of family members, agreement status (Active/Inactive), reward units, and aggregated counts of different subscription types (postpaid, MBB, fixed broadband, telephony, Fiber/Coax/TV/IP phone CDKs) owned by customers under these agreements. The data is intended for loading into 'MJØSA'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[ODS.AGREEMENT_ODS_MOB]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[ODS.AGREEMENT_MEMBER_CUSTOMER_MOB]]
- ← [[CLM_ADM.ADM_FB_ACCESSES_CUST_HIST]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]

