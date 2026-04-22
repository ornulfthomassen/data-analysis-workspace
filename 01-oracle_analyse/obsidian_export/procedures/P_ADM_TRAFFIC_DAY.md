# P_ADM_TRAFFIC_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_TRAFFIC_DAY`, aggregates daily telecommunications traffic data (MMS, SMS, Voice calls, and Data usage/revenue) for a specified month (`P_YYYYMM`). It calculates various metrics such as net revenue, number of events, call minutes, and data volume (in MB), broken down by service type (MMS, SMS, Voice, Data), data package types, and roaming status. The aggregated data is first stored in a temporary staging table (`TMP_TRAFFIC_DAY`). Subsequently, this temporary table's content is used to update or create a specific monthly partition in a permanent master traffic table (`ADM_TRAFFIC_DAY`) using a partition exchange operation. The procedure also manages the creation of new partitions if they don't exist and drops the temporary table after use.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[GALAXY.TRAFFIC_DAY_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

## Target Tables (Outputs)
- → [[TMP_TRAFFIC_DAY]]
- → [[ADM_TRAFFIC_DAY]]

