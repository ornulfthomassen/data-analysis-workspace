# P_ADM_CUSTOMER_CORE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes customer-related data for a specified month (P_YYYYMM) and loads it into a monthly partition of the 'ADM_CUSTOMER_CORE' table. It uses a partition exchange mechanism: it first creates a temporary table ('TMP_CUSTOMER_CORE') with the processed data, then swaps this temporary table's content into the target partition of 'ADM_CUSTOMER_CORE', and finally analyzes the new partition. It also handles partition creation and checks for existing data to prevent unintended overwrites.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| SUBOBJECT_NAME |
| OWNER |
- ← [[ADM_CUSTOMER_CORE]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_CORE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_DATE |
| CUSTOMER_BUCKET |
| CUSTOMER_SK |
| MONTH_CUSTOMER_SK |
| NEXT_MONTH_CUSTOMER_SK |
- → [[ADM_CUSTOMER_CORE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_DATE |
| CUSTOMER_BUCKET |
| CUSTOMER_SK |
| MONTH_CUSTOMER_SK |
| NEXT_MONTH_CUSTOMER_SK |

