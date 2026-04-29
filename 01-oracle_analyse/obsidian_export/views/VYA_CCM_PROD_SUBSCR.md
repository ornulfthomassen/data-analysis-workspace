# VYA_CCM_PROD_SUBSCR

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and prepares product subscription data from the `CCM_PRODUCT_SUBSCRIPTION_V` source for loading into the Viya/Mjøsa system, ensuring the start date is not earlier than 1970-01-01.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| LOAD_DTTM |
| PRODUCT_ID |
| BUSINESS_AREA_ID |
| START_DATE |
| END_DATE |
| SOURCE_SYSTEM_ID |

