# KIM_ORDER_ID_TO_NUM

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in the RESPONS_COPY table and updates the SOURCE_ORDER_ID column in the KIM_CUSTOMER_RESPONSE table. The update is performed for rows where CUST_RESPONSE_KEY matches between the two tables, effectively synchronizing or transferring SOURCE_ORDER_ID values. Changes are committed in batches of 1000 records.

## Data Sources (Inputs)
- ← [[RESPONS_COPY]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| SOURCE_ORDER_ID |

## Target Tables (Outputs)
- → [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| SOURCE_ORDER_ID |

