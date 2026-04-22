# CUST_HH_TAB_CRM_ANA_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure serves as a data migration and transformation utility. It migrates customer household data from a source table (`P_TABLE_OLD`) in the `CRM_ANALYSE` schema to a new, partitioned target table (`P_TABLE_NEW`) in the `CLM_ADM` schema. The process is performed incrementally by `PERIOD_MONTH_KEY` for a specified date range. It dynamically creates the target table structure, adds partitions, populates each partition using a temporary intermediate table (`P_TMP_TABLE`) and an `EXCHANGE PARTITION` strategy, and logs the migration progress and status.

## Data Sources (Inputs)
- ← [[ALL_TAB_COLS]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[[P_FRA_SCHEMA].[P_TABLE_OLD]]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_[PERIOD_MONTH_KEY]]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
- ← [[CRM_ANALYSE.RM_HOUSEHOLD_INFO_HIST]]
- ← [[ADM_MIGRATE_LOG]]

## Target Tables (Outputs)
- → [[[P_TIL_SCHEMA].[P_TABLE_NEW]]]
- → [[[P_TMP_TABLE]]]
- → [[ADM_MIGRATE_LOG]]

