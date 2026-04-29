# P_ADM_HOUSEHOLD_MAPPING_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Maintains and updates the `ADM_HOUSEHOLD_MAPPING_HIST` table for a specified month (`P_PERIOD_MONTH_KEY`). It first aggregates customer information from source tables to derive household address and unit IDs. Then, it identifies existing household mappings from the previous period, new household address mappings, and new household unit mappings. These identified mappings are consolidated into a series of temporary tables and finally into a master temporary table. This master temporary table is then used to exchange a partition in the `ADM_HOUSEHOLD_MAPPING_HIST` table, effectively adding or replacing the data for the given period. The procedure also handles partition creation and index rebuilding, and logs its activities.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| FIRST_PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| FARID |
| POSTNR |
| KURT_ID |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PREV1_PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| MAP_STATUS |
- ← [[TMP_HOUSEHOLD_MAPPING_RAW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- ← [[TMP_HOUSEHOLD_MAPPING_EXISTING]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- ← [[TMP_HOUSEHOLD_MAPPING_NEW_ADDR]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- ← [[TMP_HOUSEHOLD_MAPPING_NEW_UNIT]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |

## Target Tables (Outputs)
- → [[TMP_HOUSEHOLD_MAPPING_RAW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- → [[TMP_HOUSEHOLD_MAPPING_EXISTING]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- → [[TMP_HOUSEHOLD_MAPPING_NEW_ADDR]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- → [[TMP_HOUSEHOLD_MAPPING_NEW_UNIT]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- → [[TMP_HOUSEHOLD_MAPPING]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |
- → [[ADM_HOUSEHOLD_MAPPING_HIST]]
| Column Name |
|---|
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ADDR_ID |
| HOUSEHOLD_UNIT_ID |
| NO_ADDRESSES |
| NO_CUSTOMERS |

