# P_ADM_NPS_CS_HIST_RAW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure loads and updates monthly Net Promoter Score (NPS) Customer Satisfaction (CS) historical raw data into a permanent, partitioned target table. It achieves this by first creating a temporary staging table (`TMP_NPS_CS_HIST_RAW`), populating it with processed data from various source tables, and then using an `ALTER TABLE ... EXCHANGE PARTITION` operation to efficiently swap the temporary table's data into the corresponding monthly partition of the main `ADM_NPS_CS_HIST_RAW` table. It includes logic to check for existing partitions, handle overwrite conditions, and manage the lifecycle of the temporary table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_NPS_CS_HIST_<YYYYMM>_RAW]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]

## Target Tables (Outputs)
- → [[ADM_NPS_CS_HIST_RAW]]
- → [[TMP_NPS_CS_HIST_RAW]]

