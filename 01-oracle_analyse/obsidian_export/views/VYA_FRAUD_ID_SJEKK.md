# VYA_FRAUD_ID_SJEKK

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of service order and customer identification details, including status and action types, specifically for fraud investigation purposes.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| DEALER_ID |
| ORDER_ID |
| ORDER_ARRIVAL_DATE |
| IDENTIFICATION_NUM |
| IDENTIFICATION_TYPE_ID |
| CUST_TYPE_ID |
| CUST_BIRTHDATE |
| CUST_COMPANY_ID |
| USER_ID |
| ORDER_STATUS_ID |
| ORDER_STATUS_REASON_ID |
| ORDER_ACTION_TYPE_ID |
- ← [[CCDW_ORDER.ORDER_STATUS]]
| Column Name |
|---|
| SOURCE_ORDER_STATUS_NAME |
| SOURCE_SYSTEM_KEY |
- ← [[CCDW_ORDER.ORDER_STATUS_REASON]]
| Column Name |
|---|
| STATUS_REASON_DESC |
| STATUS_REASON |
- ← [[CCDW_ORDER.ORDER_ACTION_TYPE]]
| Column Name |
|---|
| ORDER_ACTION_TYPE_DESC |
| ORDER_ACTION_TYPE_NAME |

