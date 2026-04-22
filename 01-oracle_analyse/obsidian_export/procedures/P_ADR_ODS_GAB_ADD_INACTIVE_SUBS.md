# P_ADR_ODS_GAB_ADD_INACTIVE_SUBS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_ADR_ODS_GAB_ADD_INACTIVE_SUBS`) is designed to extract, transform, and load (ETL) data related to inactive subscriptions into a target table, `ODS_GAB_ADD_INACTIVE_SUBS`. It identifies inactive products across various technologies (DSL, FWA/FMBB, COAX, FIBER, TV) and aggregates their counts and latest inactive dates by `GAB_FLAT` and `GAB_NUMBER` (likely address or group identifiers). The procedure implements a 'hot swap' or 'blue-green deployment' strategy to update the main target table with minimal downtime. It first loads new data into a temporary staging table, builds indexes on it, and then atomically renames it to become the new main table, while the old main table is either dropped or retained as a backup. It includes logic for managing table existence, statistics, indexes, and error logging.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_FAR_GROUP]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_ADDRESS]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ALL_TABLES]]
- ← [[ALL_INDEXES]]

## Target Tables (Outputs)
- → [[ODS_GAB_ADD_INACTIVE_SUBS]]
- → [[ODS_GAB_ADD_INACTIVE_SUBS_N]]
- → [[ODS_GAB_ADD_INACTIVE_SUBS_O]]
- → [[ODS_GAB_ADD_INACTIVE_SUBS_TEMP]]

