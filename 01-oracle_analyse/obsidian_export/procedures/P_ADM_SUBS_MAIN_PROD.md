# P_ADM_SUBS_MAIN_PROD

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_SUBS_MAIN_PROD` dynamically creates or recreates a permanent table named `CLM_ADM.ADM_SUBS_MAIN_PROD`. This table serves as a reporting or data mart table, storing aggregated subscription-related product information for a specific month (determined by the input parameter `P_YYYYMM` or default). It populates this table by joining several operational and data warehouse tables to derive subscription IDs, product keys, and validity dates. After the table is created and populated, the procedure collects statistics on it to optimize query performance and grants `SELECT` privileges to the `CRM_ANALYSE` user/role.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[ADM_SUBS_MAIN_PROD]]

