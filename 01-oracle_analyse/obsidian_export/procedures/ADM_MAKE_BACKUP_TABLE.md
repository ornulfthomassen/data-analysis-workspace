# ADM_MAKE_BACKUP_TABLE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADM_MAKE_BACKUP_TABLE`, is designed to rename an existing database table and its associated indexes. It effectively archives the original table by giving it a new name. The procedure performs several validation checks, including ensuring the old table name is provided, the new table name is valid (not null, sufficient length, starts with a character, no illegal characters), the new name is different from the old, the old table exists, and that no table already exists with the new name. It also verifies that all proposed new index names are available. If all checks pass, it executes `ALTER TABLE ... RENAME TO ...` and `ALTER INDEX ... RENAME TO ...` statements to rename the table and its indexes.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[DBA_IND_COLUMNS]]

