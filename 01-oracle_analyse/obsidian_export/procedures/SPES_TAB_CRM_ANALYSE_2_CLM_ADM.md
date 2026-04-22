# SPES_TAB_CRM_ANALYSE_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `SPES_TAB_CRM_ANALYSE_2_CLM_ADM`, is designed to migrate and transform customer and subscription data on a monthly basis. It iterates through a specified date range (P_YYYYMM_FRA to P_YYYYMM_TIL) and for each month, it processes data from a source partitioned table (P_TABLE_OLD, typically in CRM_ANALYSE schema). The procedure dynamically creates a new target partitioned table (P_TABLE_NEW, in CLM_ADM schema) if it does not exist, defining its structure based on the source table's columns and additional custom customer/subscription-related columns. It then populates a temporary staging table (P_TMP_TABLE) by selecting and transforming data from the source table, performing lookups against ADM_SUBSCRIPTION_MASTER_HIST and monthly ADM_CUSTOMER_MAPPING tables to derive new customer keys (V_CUST_COLUMN1 to V_CUST_COLUMN9). After populating and modifying the temporary table (setting columns to NOT NULL), it performs an `ALTER TABLE ... EXCHANGE PARTITION` operation, swapping the temporary table with a corresponding partition in the permanent target table. The process includes logging of migration steps and status into ADM_MIGRATE_LOG and updates table statistics.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[ALL_TAB_COLS]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CRM_ANALYSE.P_TABLE_OLD]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_YYYYMM]]
- ← [[ADM_MIGRATE_LOG]]

## Target Tables (Outputs)
- → [[CLM_ADM.P_TABLE_NEW]]
- → [[P_TMP_TABLE]]
- → [[ADM_MIGRATE_LOG]]

