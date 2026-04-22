# P_ADM_CUSTOMER_DETAIL_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_CUSTOMER_DETAIL_HIST populates or updates a specific monthly partition in the `ADM_CUSTOMER_DETAIL_HIST` table. It gathers detailed customer subscription data for a given month (P_YYYYMM) by joining information from subscription history, aggregated subscription data, and product dimensions. It calculates metrics for both customer owners and users of subscriptions, such as the number of mobile subscriptions, main subscription details (MB usage, net fee, net use), and previously BankID usage (currently commented out). The data is first built into a temporary table and then efficiently moved into the target partitioned table using an `EXCHANGE PARTITION` operation. It includes checks for data availability in source tables and error handling.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_DETAIL_HIST]]
- → [[TMP_CUSTOMER_DETAIL_HIST]]

