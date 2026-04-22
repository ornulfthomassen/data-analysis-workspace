# P_FETCH_ADM_CUSTOMER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure dynamically creates a series of permanent historical tables for customer data, each specific to a monthly period. It iterates through predefined month key ranges (202207-202212, 202301-202312, and 202401-202408). For each month, it constructs a target table name (e.g., 'ADM_CUSTOMER_202301'), checks if a table with that name already exists in the 'CLM_ADM' schema, drops it if it does, and then creates a new table with the same name. This new table is populated with all data from the 'CCM.VYA_ADM_CUSTOMER' source table, filtered for the corresponding 'PERIOD_MONTH_KEY'. The process includes extensive logging of creation and row counts, and raises errors if tables are not created or are empty.

## Data Sources (Inputs)
- ← [[CCM.VYA_ADM_CUSTOMER]]
- ← [[ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_YYYYMM]]

