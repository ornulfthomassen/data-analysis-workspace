# P_SAS_LD_ADM_CUSTOMER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_SAS_LD_ADM_CUSTOMER loads historical customer data into a staging table. It iterates through the last 26 months (from the current month up to 25 months prior). In the first iteration (for the oldest month, 25 months ago), it truncates the target staging table `CLM_ADM.TMP_CHURN_ADM_CUSTOMER` and inserts the data for that month. For all subsequent 25 months, it appends the data from each corresponding monthly source table (`CLM_ADM.ADM_CUSTOMER_YYYYMM`) into the same staging table. This effectively consolidates 26 months of customer data into a single staging table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_YYYYMM]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CHURN_ADM_CUSTOMER]]

