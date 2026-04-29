# P_ADM_CUST_HOUSEHOLD_MAPP_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure populates a partitioned history table, ADM_CUST_HOUSEHOLD_MAPP_HIST, with customer and household mapping data for a specified month (P_YYYYMM). It performs data validation against `GALAXY.DATE_DIM_MV`, creates a temporary table (`TMP_CUST_HOUSEHOLD_MAPP_HIST`) by joining customer and household mapping information from `CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST`, `CLM_ADM.ADM_CUSTOMER_MAPPING_HIST`, and `CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST`. Finally, it exchanges this temporary table as a new partition into the main target history table, `ADM_CUST_HOUSEHOLD_MAPP_HIST`, for the given month.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[ADM_CUST_HOUSEHOLD_MAPP_HIST]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| PERIOD_MONTH_KEY |
| HOUSEHOLD_SK |

## Target Tables (Outputs)
- → [[TMP_CUST_HOUSEHOLD_MAPP_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| HOUSEHOLD_SK |
- → [[ADM_CUST_HOUSEHOLD_MAPP_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| HOUSEHOLD_SK |

