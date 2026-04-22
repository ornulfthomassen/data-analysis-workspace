# P_SCD2_USER_SERVICES_PHONES

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure implements a daily Slowly Changing Dimension Type 2 (SCD2) process for user service phone numbers. For each new file date, it identifies new active records, records that remain active, and records that have become inactive (ceased to be current). It then populates two temporary tables: one for the updated set of 'current' records and another for the complete set of 'past' (historical) records. Finally, it uses partition exchange to efficiently replace the 'current' and 'past' partitions of the main SCD2 table with the newly generated data, thereby maintaining a complete history of user service phone numbers with their respective `FIRST_DATE` and `LAST_DATE` and `CURRENT_RECORD` status.

## Data Sources (Inputs)
- ← [[SCD2_USER_SERVICES_PHONES]]
- ← [[COMOYO.USER_SERVICES_PHONES]]

## Target Tables (Outputs)
- → [[SCD2_USER_SERVICES_PHONES]]
- → [[TMP_SCD2_USER_SERVICES_P_C_REC]]
- → [[TMP_SCD2_USER_SERVICES_P_P_REC]]

