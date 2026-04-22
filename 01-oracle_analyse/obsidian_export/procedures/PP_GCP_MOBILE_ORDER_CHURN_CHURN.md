# PP_GCP_MOBILE_ORDER_CHURN_CHURN

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and populates mobile order churn data into a partitioned target table, `GCP_MOBILE_ORDER_CHURN_CHURN`, for a specified range of months. It processes three types of churn ('DEVICE AGREEMENT', 'PERSONAL AGREEMENT', and 'SUBSCRIPTION') by creating temporary staging tables for each type. Data is extracted from a source table (`CLM_ADM.GCP_MOBILE_ORDER_LINE`), filtered based on specific criteria for each churn type and month, loaded into these temporary tables, and then exchanged with corresponding subpartitions of the main target table. The procedure also handles the creation of partitions in the target table if they do not already exist for the processing month.

## Data Sources (Inputs)
- ← [[CLM_ADM.GCP_MOBILE_ORDER_LINE]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[GCP_MOBILE_ORDER_CHURN_CHURN]]
- → [[TMP_ORDER_LINE_MOB_CHURN_AGRM_DEVICE]]
- → [[TMP_ORDER_LINE_MOB_CHURN_AGRM_PERSONAL]]
- → [[TMP_ORDER_LINE_MOB_CHURN_SUBSCRIPTION]]

