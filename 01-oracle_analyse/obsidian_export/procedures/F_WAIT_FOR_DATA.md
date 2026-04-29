# F_WAIT_FOR_DATA

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Waits for a 'DATA_IS_FRESH' flag to become true in a specified view or table. It reads the 'DATA_IS_FRESH' value, and if it's 0, the function pauses for a defined interval and re-checks (though the current implementation only fetches once from the cursor). This process repeats until the flag is non-zero or a total timeout is reached. It returns 1 if data became fresh within the timeout, otherwise 0.

## Data Sources (Inputs)
- ← [[P_TMP_VIEW]]
| Column Name |
|---|
| DATA_IS_FRESH |

