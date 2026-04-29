# KIM_CUSTOMER_RESPONSE_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates existing customer response records in the `CRM_ANALYSE.KIM_CUSTOMER_RESPONSE` table. It identifies records to update by joining with `CICDM.CI_CUST_RESPONSE_HISTORY` based on several key fields and a more recent `PROCESSED_DTTM` in the history table. The procedure then updates specific response-related attributes in `KIM_CUSTOMER_RESPONSE` with values from the history table.

## Data Sources (Inputs)
- ← [[CICDM.CI_CUST_RESPONSE_HISTORY]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| TREATMENT_SK |
| KURT_ID |
| RESPONSE_DTTM |
| RESPONSE_CD |
| PROCESSED_DTTM |
| RESPONSE_CHANNEL_CD |
| INFERRED_RESPONSE_FLG |
| EXTERNAL_RESPONSE_INFO_ID1 |
| EXTERNAL_RESPONSE_INFO_ID2 |
| AGREE_SEND_DATE |
| AGREE_DATE |
| ORDER_SEND_DATE |
| ORDER_SYSTEM |
| SOURCE_ORDER_ID |
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| CELL_PACKAGE_SK |
| TREATMENT_SK |
| KURT_ID_OWNER |
| RESPONSE_DTTM |
| RESPONSE_CD |
| PROCESSED_DTTM |
| SOURCE_SYSTEM_KEY |
| SOURCE_ORDER_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| RESPONSE_CHANNEL_CD |
| INFERRED_RESPONSE_FLG |
| EXTERNAL_RESPONSE_INFO_ID1 |
| EXTERNAL_RESPONSE_INFO_ID2 |
| PROCESSED_DTTM |
| AGREE_SEND_DATE |
| AGREE_DATE |
| ORDER_SEND_DATE |
| ORDER_SYSTEM |
| SOURCE_ORDER_ID |

