# ADM02_HOUSEHOLD_INFO_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADM02_HOUSEHOLD_INFO_HIST`, is designed to create and/or maintain a historical, partitioned table containing aggregated household information on a monthly basis. It iterates through a specified month range (or a default range based on system date). For each month, it checks if a corresponding partition in the target historical table is populated. If not, it generates comprehensive household demographic and service subscription data by performing aggregations and transformations on source tables. This aggregated data is temporarily stored in a staging table, which is then exchanged with the relevant partition in the permanent historical table. The procedure also handles the initial creation of the main historical table, including its partitions and indexes, if it does not already exist. It logs its progress and any errors using an external history logging procedure.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[FAR.FARADR]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_HIST]]
- → [[CRM_ANALYSE.TMP_HOUSEHOLD_INFO_HIST]]

