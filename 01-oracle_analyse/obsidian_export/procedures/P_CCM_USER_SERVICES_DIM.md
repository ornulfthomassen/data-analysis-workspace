# P_CCM_USER_SERVICES_DIM

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure processes user service access data from the last 35 days. It first aggregates and categorizes this data, standardizing service names and marking services of interest, and stores the results in a temporary table named `TMP_USER_SERVICES_DIM`. Subsequently, it uses this temporary data to maintain (update existing records or insert new ones into) a permanent dimension table called `CCM_USER_SERVICES_DIM`.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_SERVICE]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[TMP_USER_SERVICES_DIM]]
- ← [[CCM_USER_SERVICES_DIM]]

## Target Tables (Outputs)
- → [[TMP_USER_SERVICES_DIM]]
- → [[CCM_USER_SERVICES_DIM]]

