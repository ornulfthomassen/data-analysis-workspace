# F_DOES_INDEX_EXIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Checks for the existence of an index with a given name within the current database schema. It counts how many objects of type 'INDEX' match the provided name (case-insensitive) and are owned by the current schema. The function returns 1 if such an index exists, and 0 otherwise.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]

