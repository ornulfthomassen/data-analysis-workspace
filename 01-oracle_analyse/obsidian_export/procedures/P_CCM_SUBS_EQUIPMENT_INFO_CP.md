# P_CCM_SUBS_EQUIPMENT_INFO_CP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure first checks for the existence of a table named 'CCM_SUBS_EQUIPMENT_INFO_CP' (determined by the variable V_TABLE) and drops it if it exists. It then creates this table as a permanent table, populating it with subscription and equipment information derived from a temporary source table. Finally, it creates a unique index and two non-unique indexes on the newly created table for performance optimization.

## Data Sources (Inputs)
- ← [[TMP_CCM_SUBS_EQUIPMENT_INFO]]

## Target Tables (Outputs)
- → [[CCM_SUBS_EQUIPMENT_INFO_CP]]

