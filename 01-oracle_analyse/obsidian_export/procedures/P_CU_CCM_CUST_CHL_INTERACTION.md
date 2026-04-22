# P_CU_CCM_CUST_CHL_INTERACTION

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure updates and maintains the `CCM_CUST_CHANNEL_INTERACTION` table by implementing a 'swap' mechanism. It first populates a new table named `CCM_CUST_CHANNEL_INTERACTION_N` with aggregated customer channel interaction data derived from a staging table. After validating the new data's row count against a predefined threshold, it performs a table swap: the existing `CCM_CUST_CHANNEL_INTERACTION` table is renamed to `CCM_CUST_CHANNEL_INTERACTION_O` (serving as a backup), and then `CCM_CUST_CHANNEL_INTERACTION_N` is renamed to `CCM_CUST_CHANNEL_INTERACTION`, making it the new active table. The procedure also dynamically creates indexes on the new table, adjusts index names after the swap, grants necessary permissions, and performs data retention cleanup (deletion of old records) on the staging table.

## Data Sources (Inputs)
- ← [[STG_CUST_CHL_INTERACTION]]
- ← [[CCM_CUST_CHANNEL_INTERACTION]]
- ← [[ALL_INDEXES]]

## Target Tables (Outputs)
- → [[CCM_CUST_CHANNEL_INTERACTION]]
- → [[CCM_CUST_CHANNEL_INTERACTION_N]]
- → [[CCM_CUST_CHANNEL_INTERACTION_O]]

