# ADM20_MOBILE_TRAFFIC_AGG1

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Aggregates mobile traffic data from the CDR.CDR_GENEVA table for a specific month (previous month, processed on the 6th day of the current month), calculates various metrics like duration, volume, and revenue, and stores the results in a partitioned summary table named ADM_MOBILE_TRAFFIC_AGG1. The procedure handles the creation of the main table and its partitions if they don't exist, uses a temporary table for intermediate aggregation, and then exchanges the temporary table with the relevant partition of the main table.

## Data Sources (Inputs)
- ← [[CDR.CDR_GENEVA]]
| Column Name |
|---|
| LOAD_DATE |
| CUST_ID_RESP |
| CUST_ID_PAYER |
| CUST_ID_USER |
| SUBSCR_ID |
| PRODUCT_UNIT_ID |
| CALLING_MAIN_DIRECTORY_NUMBER |
| CALLING_DIRECTORY_NUMBER |
| DESTINATION_COUNTRY_CODE |
| ROAMING_COUNTRY_CODE |
| GENEVA_CALL_TYPE |
| TIERID_1 |
| TIERID_2 |
| TIERID_3 |
| BEARER |
| GPRS_APN |
| DISCOUNT_PRODUCT_OFFER_ID |
| EDITED_B_NUMBER |
| EVENT_TIME_DURATION |
| EVENT_VOLUME |
| EVENT_START_DATE_TIME |
| RATED_EVENT_BASE_PRICE |
| RATED_EVENT_PRICE |
| DISCOUNT |
| NET_REVENUE |
| TAX_STATUS |
| TAX_RATE |
| EVENT_DELETED |
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG1]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG1]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| GENEVA_OWNER_ID |
| GENEVA_PAYER_ID |
| GENEVA_USER_ID |
| SUBSCR_ID |
| PRODUCT_UNIT_ID |
| MAIN_NUMBER_HOVED |
| MAIN_NUMBER_BRUKT |
| DESTINATION_COUNTRY_CODE |
| ROAMING_COUNTRY_CODE |
| GENEVA_CALL_TYPE |
| TIERID_1 |
| TIERID_2 |
| TIERID_3 |
| BEARER |
| APN |
| DISCOUNT_PRODUCT_OFFER_ID |
| NO_EDITED_B_NUMBER |
| EVENT_TIME_DURATION |
| BYTE_TOTALT |
| MB_TOTALT |
| EVENT_START_DATE_TIME |
| ANTALL |
| NOK |
| NOK_URABATTERT |
| NOK_RABATT |
| NET_REVENUE |
| TAX_STATUS |
| TAX_RATE |
- → [[CLM_ADM.TMP_MOBILE_TRAFFIC_AGG1]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| GENEVA_OWNER_ID |
| GENEVA_PAYER_ID |
| GENEVA_USER_ID |
| SUBSCR_ID |
| PRODUCT_UNIT_ID |
| MAIN_NUMBER_HOVED |
| MAIN_NUMBER_BRUKT |
| DESTINATION_COUNTRY_CODE |
| ROAMING_COUNTRY_CODE |
| GENEVA_CALL_TYPE |
| TIERID_1 |
| TIERID_2 |
| TIERID_3 |
| BEARER |
| APN |
| DISCOUNT_PRODUCT_OFFER_ID |
| NO_EDITED_B_NUMBER |
| EVENT_TIME_DURATION |
| BYTE_TOTALT |
| MB_TOTALT |
| EVENT_START_DATE_TIME |
| ANTALL |
| NOK |
| NOK_URABATTERT |
| NOK_RABATT |
| NET_REVENUE |
| TAX_STATUS |
| TAX_RATE |

