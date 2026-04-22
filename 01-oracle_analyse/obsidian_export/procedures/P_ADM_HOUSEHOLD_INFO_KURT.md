# P_ADM_HOUSEHOLD_INFO_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_HOUSEHOLD_INFO_KURT creates or recreates the 'ADM_HOUSEHOLD_INFO_KURT' table by aggregating customer and household demographic and service information for the previous month. It performs initial checks on source data availability. Before creating the new table, it renames any existing 'ADM_HOUSEHOLD_INFO_KURT' table to 'ADM_HOUSEHOLD_INFO_KURT_OLD' (acting as a backup) and may drop an older 'ADM_HOUSEHOLD_INFO_KURT_OLD' if it exists. The new 'ADM_HOUSEHOLD_INFO_KURT' table is then populated with detailed household-level aggregations derived from 'CLM_ADM.ADM_CUSTOMER_INFO_KURT'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_KURT]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]

## Target Tables (Outputs)
- → [[ADM_HOUSEHOLD_INFO_KURT]]
- → [[ADM_HOUSEHOLD_INFO_KURT_OLD]]

