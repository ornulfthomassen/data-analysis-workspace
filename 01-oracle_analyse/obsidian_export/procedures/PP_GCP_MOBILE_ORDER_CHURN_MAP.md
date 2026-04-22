# PP_GCP_MOBILE_ORDER_CHURN_MAP

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `PP_GCP_MOBILE_ORDER_CHURN_MAP` procedure calculates and maps mobile order churn events to corresponding sales events within a 70-day window. For each month in a specified range (defaulting to the month three months prior to the current date), it performs the following steps:
1.  It checks if a specific partition for the current processing month exists in the `GCP_MOBILE_ORDER_CHURN_MAP` table. If not, it creates that partition.
2.  It creates an intermediate temporary table, `TMP_ORDER_CHURN_MAP_JOIN`, by joining sales order data (`GCP_MOBILE_ORDER_CHURN_SALES`) with churn order data (`GCP_MOBILE_ORDER_CHURN_CHURN`). This join identifies churn events that occur within 70 days of a sales event, categorizing them by 'Abonnement' (Subscription) or 'Avtale' (Agreement) based on specific sales and churn types. It also calculates churn duration in seconds and days, and assigns churn day categories (0-14, 15-70, 0-70 days).
3.  Finally, it replaces the content of the corresponding partition in the permanent target table `GCP_MOBILE_ORDER_CHURN_MAP` with the data from the temporary `TMP_ORDER_CHURN_MAP_JOIN` table using an `ALTER TABLE ... EXCHANGE PARTITION` statement, thereby integrating the processed churn-to-sales mapping data.

## Data Sources (Inputs)
- ← [[CLM_ADM.GCP_MOBILE_ORDER_CHURN_SALES]]
- ← [[CLM_ADM.GCP_MOBILE_ORDER_CHURN_CHURN]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CLM_ADM.GCP_MOBILE_ORDER_CHURN_MAP]]
- → [[CLM_ADM.TMP_ORDER_CHURN_MAP_JOIN]]

