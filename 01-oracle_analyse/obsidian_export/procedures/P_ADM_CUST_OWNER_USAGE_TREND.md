# P_ADM_CUST_OWNER_USAGE_TREND

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates monthly usage trends and various metrics for customer owners over a 7-month historical period (current month and six preceding months). The aggregated trend data is then loaded into a specific partition of the `ADM_CUSTOMER_OWNER_USAGE_TREND` table, utilizing a dynamically created temporary table (`TMP_CUSTOMER_OWNER_USAGE_TREND`) for intermediate calculations and an efficient partition exchange operation for data loading. The procedure includes checks for table existence, existing partition data, and source data availability.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[ADM_CUSTOMER_OWNER_USAGE_TREND]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_OWNER_USAGE_TREND]]
- → [[TMP_CUSTOMER_OWNER_USAGE_TREND]]

