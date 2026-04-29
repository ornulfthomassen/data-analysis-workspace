# TCX_CONFIG_TRG

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Automatically assigns a unique identifier from the `CCM.TCX_CONFIG_SEQ` sequence to the `CONFIG_ID` column of a new record in the `CCM.TCX_CONFIG` table before insertion.

## Data Sources (Inputs)
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CCM.TCX_CONFIG]]
| Column Name |
|---|
| CONFIG_ID |

