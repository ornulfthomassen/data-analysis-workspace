# PP_GCP_MOBILE_ORDER_CHURN_SALES

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `PP_GCP_MOBILE_ORDER_CHURN_SALES`, processes mobile order line sales data from a source table (`CLM_ADM.GCP_MOBILE_ORDER_LINE`) for a specified range of months. For each month, it first ensures that a corresponding partition exists in the main target table (`GCP_MOBILE_ORDER_CHURN_SALES`). It then categorizes the sales data into three types: 'Device Agreement' (DA), 'Personal Agreement' (PA), and 'Subscription' (S). For each sales type, it creates a dedicated temporary table, populates it with filtered and transformed data from the source table, gathers statistics on this temporary table, and finally exchanges the content of this temporary table with the respective subpartition within the `GCP_MOBILE_ORDER_CHURN_SALES` table. The procedure essentially loads and categorizes mobile sales order data into a partitioned target table.

## Data Sources (Inputs)
- ← [[CLM_ADM.GCP_MOBILE_ORDER_LINE]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[GCP_MOBILE_ORDER_CHURN_SALES]]
- → [[TMP_ORDER_LINE_MOB_SALES_AGRM_DEVICE]]
- → [[TMP_ORDER_LINE_MOB_SALES_AGRM_PERSONAL]]
- → [[TMP_ORDER_LINE_MOB_SALES_SUBSCRIPTION]]

