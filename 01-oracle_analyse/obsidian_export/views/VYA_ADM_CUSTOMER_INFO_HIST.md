# VYA_ADM_CUSTOMER_INFO_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYA_ADM_CUSTOMER_INFO_HIST`, consolidates historical customer and household demographic and status information. It prepares time-sliced data (based on `PERIOD_MONTH_KEY`) by joining core customer details with monthly dimension data and household information. The view calculates derived attributes like age-based segments and composite keys, while filtering for specific customer types, statuses, and excluding a list of particular customer IDs. It is intended for loading historical customer data into an analytical system or data warehouse named 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| AGE |
| GENDER |
| MONTH_OF_BIRTH |
| EMAIL_IND |
| SMS_IND |
| RES_BRSUND_TM |
| RES_BRSUND_DM |
| RES_TELENOR_TM |
| RES_TELENOR_DM |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
| ANTALL_I_HUSSTAND |
| POSTADR_POSTNR |
| POSTNR |
| KOMMUNENR |
| GRUNNKRETS_NR |
| BOLIGTYPE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ADDR_SK |
| PERIOD_MONTH_KEY |
| HOUSEHOLD_UNIT_SK |
| MIN_AGE |
| NO_00_TO_05 |
| NO_06_TO_12 |
| NO_13_TO_17 |
| NO_18_TO_28 |
| NO_29_TO_49 |
| NO_50_TO_66 |
| NO_67_AND_ABOVE |

