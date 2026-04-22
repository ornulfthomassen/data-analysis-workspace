# P_ADM_CLM_SEGMENT_CUSTOMER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure manages a partitioned customer segment table named 'CLM_ADM.ADM_CLM_SEGMENT_CUSTOMER'. It first checks if this table exists. If not, it creates the table with specific columns, sets it up for list partitioning by 'PERIOD_MONTH_KEY', enables NOLOGGING, and creates an index ('IX_CA_SEGMENT_CUSTOMER_KID'). Subsequently, it determines a range of months (YYYYMM) for processing, based on input parameters or system date. For each month within this range, it dynamically drops (if existing) and then adds a new partition to the 'CLM_ADM.ADM_CLM_SEGMENT_CUSTOMER' table. It then populates this new partition by inserting segmented customer data, which is derived by joining household information from 'CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST' and 'CRM_ANALYSE.ADM_HOUSEHOLD_INFO_HIST' with data from a dynamically named analytic universe view (e.g., 'CRM_ANALYSE.V_BR_ANALYTIC_UNIVERSE_YYYYMM'). The 'CLM_LIVSFASE' field is calculated using a custom function 'CRM_ANALYSE.FORMAT_CLM_LIVSFASE_SEGMENT'. After each month's data insertion, it commits the changes and gathers statistics for the newly loaded partition. It also handles the optional dropping and recreation of indexes for performance during bulk loading.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_HIST]]
- ← [[CRM_ANALYSE.V_BR_ANALYTIC_UNIVERSE_]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CLM_SEGMENT_CUSTOMER]]

