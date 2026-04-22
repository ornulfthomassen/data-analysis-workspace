# P_ADM_CUSTOMER_MAPPING_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Manages the historical, partitioned table `ADM_CUSTOMER_MAPPING_HIST` for a specific month. It extracts customer mapping data from `CCDW.CUSTOMER_MAPPING`, stages it into a temporary table (`TMP_CUSTOMER_MAPPING_HIST`), and then uses an `ALTER TABLE ... EXCHANGE PARTITION` operation to update or add a partition in `ADM_CUSTOMER_MAPPING_HIST` with this new data. The procedure also handles partition existence checks, partition creation, index drops and creations (on `ADM_CUSTOMER_MAPPING_HIST`), and gathers statistics for the updated partition. It prevents overwriting existing data unless explicitly allowed.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CCDW.CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- → [[CLM_ADM.TMP_CUSTOMER_MAPPING_HIST]]

