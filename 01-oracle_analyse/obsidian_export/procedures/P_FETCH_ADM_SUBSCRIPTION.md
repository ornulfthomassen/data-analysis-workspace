# P_FETCH_ADM_SUBSCRIPTION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_FETCH_ADM_SUBSCRIPTION extracts and processes detailed administrative subscription data for both the current and previous months. It dynamically creates two permanent snapshot tables (e.g., ADM_SUBSCRIPTION_YYYYMM for previous month and ADM_SUBSCRIPTION_YYYYMM for current month) in the CLM_ADM schema. Each table stores a distinct set of comprehensive subscription attributes, product information, device details, usage statistics, and financial metrics. The procedure drops existing snapshot tables for the respective months if they already exist, then populates new ones by selecting data from source tables (CCM.VYA_ADM_SUBSCRIPTION for previous month and CCM.VYA_ADM_SUBSCRIPTION_CURRENT for current month). It includes logging of table creation and row counts, and raises an error if the newly created target tables are empty.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[ALL_OBJECTS]]
- ← [[CCM.VYA_ADM_SUBSCRIPTION]]
- ← [[CCM.VYA_ADM_SUBSCRIPTION_CURRENT]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_SUBSCRIPTION_YYYYMM (previous month)]]
- → [[CLM_ADM.ADM_SUBSCRIPTION_YYYYMM (current month)]]

