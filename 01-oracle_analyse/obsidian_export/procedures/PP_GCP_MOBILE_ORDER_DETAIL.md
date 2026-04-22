# PP_GCP_MOBILE_ORDER_DETAIL

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `PP_GCP_MOBILE_ORDER_DETAIL` dynamically manages and populates monthly partitions of the `GCP_MOBILE_ORDER_DETAIL` table. For a given range of months (determined by `P_YYYYMM_FRA` and `P_YYYYMM_TIL` or calculated based on `SYSDATE`), it first ensures that the target partition exists within `GCP_MOBILE_ORDER_DETAIL`. It then creates a staging table (`TMP_MOBILE_ORDER_DETAIL`) by joining and transforming detailed mobile order line data from `GCP_MOBILE_ORDER_LINE` with churn mapping information from `GCP_MOBILE_ORDER_CHURN_MAP`. This process involves applying complex business logic to calculate various Key Performance Indicators (KPIs) and descriptive attributes. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently load the processed data from the staging table into the corresponding monthly partition of `GCP_MOBILE_ORDER_DETAIL`. The staging table serves as a temporary work area, being explicitly dropped and recreated for each execution or loop iteration, and its data is migrated to the final target table.

## Data Sources (Inputs)
- ← [[GCP_MOBILE_ORDER_LINE]]
- ← [[GCP_MOBILE_ORDER_CHURN_MAP]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]

## Target Tables (Outputs)
- → [[GCP_MOBILE_ORDER_DETAIL]]
- → [[TMP_MOBILE_ORDER_DETAIL]]

