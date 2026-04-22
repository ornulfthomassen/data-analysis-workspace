# P_ADR_ODS_FAR_GROUP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure `P_ADR_ODS_FAR_GROUP` is designed to refresh a main target table (`ODS_FAR_GROUP`) with new data extracted from a source, using a 'hot swap' mechanism. It involves creating a temporary staging table (`ODS_FAR_GROUP_N`), populating it with processed data, and then renaming it to become the new main table. Concurrently, the old main table is renamed to a backup table (`ODS_FAR_GROUP_O`). The procedure performs checks for table existence, gathers statistics, manages indexes (creating them on the new staging table and renaming them during the swap), and verifies data volume changes against a configurable threshold (`V_RANGE_SWAP`) to prevent unintended swaps. All significant actions, warnings, and errors are logged to history tables.

## Data Sources (Inputs)
- ← [[ALL_TABLES]]
- ← [[ALL_INDEXES]]
- ← [[USER_INDEXES]]
- ← [[DUAL]]
- ← [[CLM_CCM.ODS_FAR]]

## Target Tables (Outputs)
- → [[ODS_FAR_GROUP]]
- → [[ODS_FAR_GROUP_N]]
- → [[ODS_FAR_GROUP_O]]
- → [[ODS_FAR_GROUP_O_TEMP]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]

