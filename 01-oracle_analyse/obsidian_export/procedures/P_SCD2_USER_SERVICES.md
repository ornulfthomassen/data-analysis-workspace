# P_SCD2_USER_SERVICES

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_SCD2_USER_SERVICES` implements a Slowly Changing Dimension (SCD) Type 2 strategy for user service data. It processes daily snapshots of user services, identified by `FILE_DATE`, from the `COMOYO.USER_SERVICES` table. The goal is to maintain a historical and current view of user services in the `SCD2_USER_SERVICES` table, which is partitioned. For each processing date, it generates two temporary tables: `TMP_SCD2_USER_SERVICES_C_REC` contains the updated set of 'current active' records (new active users and existing active users with updated `LAST_DATE`), and `TMP_SCD2_USER_SERVICES_P_REC` contains the updated set of 'past/historical' records (existing historical records and records that have transitioned from an active-inactive state to a historical state). These temporary tables are then used to replace the corresponding partitions (`CURRENT_REC` and `PAST_REC`) within the `SCD2_USER_SERVICES` table, ensuring historical tracking of user service states.

## Data Sources (Inputs)
- ← [[SCD2_USER_SERVICES]]
- ← [[COMOYO.USER_SERVICES]]

## Target Tables (Outputs)
- → [[SCD2_USER_SERVICES]]
- → [[TMP_SCD2_USER_SERVICES_C_REC]]
- → [[TMP_SCD2_USER_SERVICES_P_REC]]

