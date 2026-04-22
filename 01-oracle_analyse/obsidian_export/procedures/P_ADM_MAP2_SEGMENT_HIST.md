# P_ADM_MAP2_SEGMENT_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_ADM_MAP2_SEGMENT_HIST`) is designed to load and maintain historical MAP2 segment data into a partitioned table, `ADM_MAP2_SEGMENT_HIST`, for a specified period (month, `P_YYYYMM`). It performs several key operations:

1.  **Data Source Validation**: It first checks the existence and integrity of required data in several source tables (`GALAXY.DATE_DIM_MV`, `CRM_ANALYSE.MAP2_SEGMENT_HIST`, `CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL`) for the target month. If source data is insufficient or invalid, it raises an error.
2.  **Partition Management**: It manages partitions within the `ADM_MAP2_SEGMENT_HIST` table. If a partition for the specified month (`V_YYYYMM`) does not exist, it creates one. If it exists, it checks if data is present and respects an overwrite flag (`P_OVERWRITE_PARTITION`).
3.  **Data Transformation and Staging**: It creates a temporary table (`TMP_MAP2_SEGMENT_HIST`) to stage and transform the data. This involves selecting and joining data from `CRM_ANALYSE.MAP2_SEGMENT_HIST` and `CLM_ADM.ADM_CUSTOMER_MAPPING`, enriching it with `PERIOD_MONTH_KEY`, `CUSTOMER_SK`, and other segment-related attributes.
4.  **Efficient Data Loading**: It uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently swap the populated temporary table with the corresponding partition in the `ADM_MAP2_SEGMENT_HIST` table. This is a common method for high-performance loading into partitioned tables.
5.  **Statistics Gathering**: After loading, it analyzes the newly loaded partition to ensure optimal query performance.
6.  **Comprehensive Logging and Error Handling**: The procedure includes extensive `DBMS_OUTPUT` logging for tracing execution and calls a custom logging procedure (`CRM_ANALYSE.P_ADM_LOAD_HISTORY`) to record progress and errors. It handles various exceptions to provide informative error messages.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.MAP2_SEGMENT_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

## Target Tables (Outputs)
- → [[ADM_MAP2_SEGMENT_HIST]]
- → [[TMP_MAP2_SEGMENT_HIST]]

