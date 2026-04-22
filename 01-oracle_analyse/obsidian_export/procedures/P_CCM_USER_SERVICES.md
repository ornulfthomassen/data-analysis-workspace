# P_CCM_USER_SERVICES

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure identifies and consolidates service access information for Norwegian users. It first extracts unique user IDs associated with Norwegian phone numbers (from `USER_SERVICES_PHONES` and `FIM_USER_PHONES`) into a temporary staging table (`CCM_USER_SERVICE_NO_TMP`). Subsequently, it uses this list of Norwegian users to process their detailed service access records from `USER_SERVICES_SERVICE_scd` and aggregated daily connection data from `MINSKY_MAIN_DAILY`. The procedure calculates the first, last, and effective last usage dates for each user's service and stores the consolidated results in a new table (`CCM_USER_SERVICES_CP`), finally creating a unique index on this table for efficient access.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_PHONES]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.MINSKY_MAIN_DAILY]]
- ← [[COMOYO.USER_SERVICES_SERVICE_scd]]
- ← [[CCM_USER_SERVICE_NO_TMP]]

## Target Tables (Outputs)
- → [[CCM_USER_SERVICE_NO_TMP]]
- → [[CCM_USER_SERVICES_CP]]

