# P_SCD2_USER_SERVICES_EMAIL

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_SCD2_USER_SERVICES_EMAIL`, implements a Slowly Changing Dimension Type 2 (SCD2) mechanism for user service email data. It processes daily snapshots of user email information from `COMOYO.USER_SERVICES_EMAIL` to maintain a historical and current record of user emails in a partitioned target table named `SCD2_USER_SERVICES_EMAIL`. For each new daily snapshot, it identifies new active emails, existing active emails, and emails that have become inactive. It stages these records into two dynamically created temporary tables (one for 'current' records and one for 'past' records) and then uses efficient partition exchange operations to update the 'CURRENT_REC' and 'PAST_REC' partitions of the main `SCD2_USER_SERVICES_EMAIL` table.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_EMAIL]]
- ← [[SCD2_USER_SERVICES_EMAIL]]

## Target Tables (Outputs)
- → [[SCD2_USER_SERVICES_EMAIL]]
- → [[TMP_SCD2_USER_SERVICES_E_C_REC]]
- → [[TMP_SCD2_USER_SERVICES_E_P_REC]]

