# P_SCD2_MIN_SKY_MAIN

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Implements a daily Slowly Changing Dimension Type 2 (SCD2) update for user activity and quota data. The procedure processes daily snapshots from the `COMOYO.MINSKY_MAIN_DAILY` table, identifies changes in user records based on attributes like connection timestamps and quotas, and updates the `CURRENT_REC` and `PAST_REC` partitions of the main `SCD2_MIN_SKY_MAIN` dimension table using temporary staging tables and Oracle's partition exchange mechanism. This ensures that a full history of user records is maintained.

## Data Sources (Inputs)
- ← [[SCD2_MIN_SKY_MAIN]]
- ← [[COMOYO.MINSKY_MAIN_DAILY]]

## Target Tables (Outputs)
- → [[SCD2_MIN_SKY_MAIN]]
- → [[TMP_MINSKY_MAIN_DAILY_CURR]]
- → [[TMP_SCD2_MIN_SKY_MAIN_CURR_REC]]
- → [[TMP_SCD2_MIN_SKY_MAIN_PAST_REC]]

