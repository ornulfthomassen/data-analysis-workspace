# ANONF_REACTIVATE_CUSTOMER_SK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle function `ANONF_REACTIVATE_CUSTOMER_SK` reactivates a customer by updating their mapping status and related metadata in the `ANON_ADM_CUSTOMER_MAPPING` table. It validates the provided `P_KURT_ID` against `KURT.KURT` and checks for its existing mapping in `ANON_ADM_CUSTOMER_MAPPING`. If the `KURT_ID` has an existing mapping, the function returns -1. Otherwise, it retrieves the current `CUSTOMER_SK` and `MAP_STATUS`. If the `MAP_STATUS` is 'EKSKUNDE', it updates the record by setting `MAP_STATUS` to 'KUNDE', updating various date fields (`STATUS_DATE`, `OWNER_START_DATE`, `USER_START_DATE`, `KURT_ID_UPDATE_DATE`), and incrementing `OWNER_NUMBER_OF_TIMES` and `USER_NUMBER_OF_TIMES`. The procedure includes error handling for validation failures and unhandled map statuses.

## Data Sources (Inputs)
- ← [[KURT.KURT]]
| Column Name |
|---|
| KID |
- ← [[ANON_ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
| MAP_STATUS |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |

## Target Tables (Outputs)
- → [[ANON_ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| MAP_STATUS |
| STATUS_DATE |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |
| KURT_ID_UPDATE_DATE |

