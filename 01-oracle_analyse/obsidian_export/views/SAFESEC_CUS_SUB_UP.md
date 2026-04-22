# SAFESEC_CUS_SUB_UP

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts a unique customer key and an associated subscription key, primarily for active 'FKM MOBIL' subscriptions. For each customer, it selects the highest-ranked subscription key available. If no matching active 'FKM MOBIL' subscription is found, the subscription key defaults to -1. The resulting customer_sk and subscription_sk are cast to CHAR types. The view is explicitly noted as being part of the reporting basis for the 'safe and secure squad'.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUST_CONTACT_PHONE]]
- ← [[clm_adm.adm_customer_mapping]]
- ← [[galaxy.subscription_dim_mv]]

