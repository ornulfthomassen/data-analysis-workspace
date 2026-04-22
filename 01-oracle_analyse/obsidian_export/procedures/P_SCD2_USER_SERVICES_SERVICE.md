# P_SCD2_USER_SERVICES_SERVICE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure implements a Type 2 Slowly Changing Dimension (SCD2) update strategy for user service data. It processes incremental data from `COMOYO.USER_SERVICES_SERVICE` to maintain a history of user service records in the partitioned `SCD2_USER_SERVICES_SERVICE` table. For each processing date, it identifies new active records, updates existing active records (by retaining unchanged ones in the 'current' partition and moving changed versions to the 'past' partition), and handles records that are no longer present in the incoming data (potentially marking them `ON_LAST_FILE='N'` in the 'current' partition). It uses temporary tables for staging the updated 'current' and 'past' data, which are then swapped into the main SCD2 table's partitions via `ALTER TABLE ... EXCHANGE PARTITION` for efficient updates.

## Data Sources (Inputs)
- ← [[SCD2_USER_SERVICES_SERVICE]]
- ← [[COMOYO.USER_SERVICES_SERVICE]]

## Target Tables (Outputs)
- → [[SCD2_USER_SERVICES_SERVICE]]
- → [[TMP_SCD2_USER_SERVICES_S_C_REC]]
- → [[TMP_SCD2_USER_SERVICES_S_P_REC]]

