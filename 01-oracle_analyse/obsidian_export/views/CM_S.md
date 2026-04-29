# CM_S

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Combines subscription details from the CM.SUBSCRIPTION table with product service mapping descriptions from the CM.PROD_SERV_MAPPING table, returning a distinct set of subscription and product-related information.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| CUST_ID_PAYER |
| CUST_ID_RESP |
| CUST_ID_USER |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
| PRODUCT_ID |
| S212_PRODUCT_ID |
- ← [[CM.PROD_SERV_MAPPING]]
| Column Name |
|---|
| PRODUCT_DESCR |
| PRODUCT_UNIT_ID |

