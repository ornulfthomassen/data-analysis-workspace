# P_ADM_GLOBAL_USER_SUBS_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_GLOBAL_USER_SUBS_HIST is designed to load and update historical user subscription data for a specific month (identified by V_YYYYMM) into a partitioned target table, CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST. It first performs a series of checks:
1.  Verifies the existence of the main target table.
2.  Checks if the target partition for the given month already exists. If it does and is not empty, it prevents overwriting unless explicitly allowed. If the partition doesn't exist, it creates a new one.
It then proceeds to create a temporary table, CLM_ADM.TMP_GLOBAL_USER_SUBS_HIST, populating it with aggregated subscription event data extracted from various source systems (CM, CCDW, COMOYO, GALAXY). After the temporary table is populated, it performs an atomic exchange of the target partition with the newly created temporary table, effectively updating the historical data. Finally, it rebuilds the associated index for the updated partition and gathers statistics. The procedure includes robust error handling and logs various stages of the process and any encountered errors using an external logging procedure.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_GLOBAL_USER_SUBS_HIST]]
- → [[CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST]]

