# P_ADM_CUSTOMER_OWNER_SUBS_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_CUSTOMER_OWNER_SUBS_AGG, is designed to aggregate customer subscription and usage data for a specified month (P_YYYYMM). It performs detailed calculations of fees, usage, and traffic metrics (data, MMS, SMS, voice) broken down by various product groups (MPP, MPR, MBB, FIX, DSL, FIBER) and customer ownership. The procedure manages a partitioned permanent table, ADM_CUSTOMER_OWNER_SUBS_AGG, adding a new partition for the target month if needed. It uses a temporary staging table, TMP_CUSTOMER_OWNER_SUBS_AGG, for intermediate aggregation results, which are then efficiently loaded into the permanent table's partition using an EXCHANGE PARTITION operation. The process includes checks for data availability in source tables and handles potential overwriting of existing partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[PD]]

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_OWNER_SUBS_AGG]]
- → [[ADM_CUSTOMER_OWNER_SUBS_AGG]]

