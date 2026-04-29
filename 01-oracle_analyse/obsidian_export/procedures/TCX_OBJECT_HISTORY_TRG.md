# TCX_OBJECT_HISTORY_TRG

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Automatically populates the TRANSACTION_ID column for new rows being inserted into the CCM.TCX_OBJECT_HISTORY table, using the next value from the CCM.TCX_OBJECT_HISTORY_SEQ sequence.

## Data Sources (Inputs)
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CCM.TCX_OBJECT_HISTORY]]
| Column Name |
|---|
| TRANSACTION_ID |

