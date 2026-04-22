# P_ADM_BILL_SHOCK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_BILL_SHOCK` processes mobile traffic data and subscription information for a specified month. It aggregates mobile packet data usage (NOK and a 'twin count') from source tables. These aggregated results are then loaded into a monthly partitioned table named `ADM_BILL_SHOCK`. It manages the existence of the target partition, creating it if it doesn't exist, and uses a temporary table (`TMP_BILL_SHOCK`) as an intermediate staging area before performing a partition exchange operation to update the main table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG]]
- ← [[ADM_SUBSCRIPTION_MASTER_HIST]]

## Target Tables (Outputs)
- → [[ADM_BILL_SHOCK]]
- → [[TMP_BILL_SHOCK]]

