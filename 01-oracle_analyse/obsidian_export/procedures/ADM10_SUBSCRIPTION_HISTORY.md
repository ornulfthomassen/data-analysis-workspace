# ADM10_SUBSCRIPTION_HISTORY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure populates or updates a monthly partitioned historical subscription fact table named `ADM_SUBSCRIPTION_HISTORY`. It iterates through a specified range of months, creating or updating a partition for each month. For each month, it extracts and processes detailed subscription-related data from various source systems, performing complex joins and aggregations to derive metrics like active days and product changes. Intermediate results are staged in transient temporary tables (`ADM_SUBSCRIPTION_HISTORY_TMP1`, `ADM_SUBSCRIPTION_HISTORY_TMP2`). The final monthly data, representing a snapshot of subscriptions, is prepared in another temporary table (`ADM_SUBSCRIPTION_HISTORY_TMP`), which is then efficiently swapped into the main partitioned table using an `ALTER TABLE ... EXCHANGE PARTITION` operation. The procedure also manages table creation, index creation/dropping, and statistics gathering, and logs its progress and any data integrity issues identified during source data validation.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[ADM_PRIM_PROD_ATTR_HIST]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_HISTORY]]
- → [[ADM_SUBSCRIPTION_HISTORY_TMP1]]
- → [[ADM_SUBSCRIPTION_HISTORY_TMP2]]
- → [[ADM_SUBSCRIPTION_HISTORY_TMP]]

