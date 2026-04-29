# GCP_SIMCARD_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a detailed and unified view of active SIM card information by joining customer, subscription, and SIM card detail tables. It categorizes customers (e.g., Service Provider, Business, Private), transforms MSISDN and product offer IDs, and includes SIM card type, status, e-SIM type, and relevant date information.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| CUST_ID_RESP |
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| S212_REF_ID |
| CUST_LAST_NAME |
| UNIT_TYPE_ID |
- ← [[CM.REL_NUMBER]]
| Column Name |
|---|
| SUBSCR_ID_OWNER |
| PRODUCT_END_DATE |
| PRODUCT_START_DATE |
| ICC_ID |
| SUBSCRIBED_OFFER_ID |
| DIRECTORY_NUMBER_ID |
| SUBSCRIPTION_SIMCARD_TYPE |
| MSISDN |
| PRODUCT_OFFER_ID |
| INFO_CHG_DATE |
- ← [[SIMNR.SIMCARD_DETAILS]]
| Column Name |
|---|
| MSISDN_ID |
| ICC_ID |
| END_DATE |
| SIMCARD_STATUS_ID |
| SERVICE_PROVIDER_ID |
| SIMCARD_TYPE_DESCR |
| SIMCARD_STATUS_DESCR |
| START_DATE |
| SIMCARD_ESIM_TYPE_NAME |
| IMSI_INTERVAL_TYPE_DESCR |
| RECORD_CHANGE_DATE |

