# P_ADM_HOUSEHOLD_MAPPING_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure P_ADM_HOUSEHOLD_MAPPING_HIST processes and manages historical household mapping data for a given month. It identifies existing household mappings, new addresses associated with existing units, and entirely new household units by comparing raw customer data for the current period with previously recorded historical data. The procedure orchestrates the creation of several temporary staging tables to perform these calculations. Finally, it loads the consolidated, categorized household mapping data for the current month into a specific partition of the `ADM_HOUSEHOLD_MAPPING_HIST` table, generating new surrogate keys (SKs) for new addresses and units while preserving existing ones.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_KURT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]

## Target Tables (Outputs)
- → [[ADM_HOUSEHOLD_MAPPING_HIST]]
- → [[TMP_HOUSEHOLD_MAPPING_RAW]]
- → [[TMP_HOUSEHOLD_MAPPING_EXISTING]]
- → [[TMP_HOUSEHOLD_MAPPING_NEW_ADDR]]
- → [[TMP_HOUSEHOLD_MAPPING_NEW_UNIT]]
- → [[TMP_HOUSEHOLD_MAPPING]]

