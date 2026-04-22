# P_ADM_SUBSCRIPTION_BANKID

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Populates a specific monthly partition of the `ADM_SUBSCRIPTION_BANKID` table with aggregated `BANKID` usage statistics for subscriptions. It first checks for source data validity and ensures the target partition either doesn't exist or is allowed to be overwritten. It then creates a temporary staging table, populates it with calculated data (subscription ID and aggregated BANKID usage over three months), and finally exchanges this temporary table with the corresponding partition in the `ADM_SUBSCRIPTION_BANKID` table. The procedure also manages partition creation and updates load history.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CONAX.FACT_BANKID]]
- ← [[CONAX.DIM_ENDUSER]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_BANKID]]
- → [[TMP_SUBSCRIPTION_BANKID]]

