# P_ADM_AGRM_SFTY_CUSTLOG_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_AGRM_SFTY_CUSTLOG_HIST serves as an ETL process to incrementally update and maintain historical customer activity logs in the partitioned table CLM_ADM.ADM_AGRM_SFTY_CUSTLOG_HIST. It identifies new customer activity data based on specific log types ('KILDE'), combines this new data with existing historical data for that type, stages the combined dataset in a temporary table, and then updates the corresponding partition in the main historical table via a partition exchange operation. It handles at least two distinct categories of customer activity logs: general activity and email verification logs.

## Data Sources (Inputs)
- ← [[CUSTOMERLOG.ACTIVITY_LOG]]
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER_LINK]]
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER]]
- ← [[CM.CUSTOMER]]
- ← [[CUSTOMERLOG.ACTIVITY_DESCRIPTION]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_AGRM_SFTY_CUSTLOG_HIST]]

## Target Tables (Outputs)
- → [[ADM_AGRM_SFTY_CUSTLOG_HIST]]
- → [[TMP_AGRM_SFTY_CUSTLOG_HIST0]]
- → [[TMP_AGRM_SFTY_CUSTLOG_HIST0_2]]

