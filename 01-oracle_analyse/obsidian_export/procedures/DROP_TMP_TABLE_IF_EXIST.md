# DROP_TMP_TABLE_IF_EXIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Checks for the existence of a table (prefixed with 'TMP_') within the current schema. If the table exists, it is dropped to prevent errors from subsequent operations or to clean up previously created temporary structures.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]

