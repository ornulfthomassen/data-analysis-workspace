# P_ADM_MOBILE_USAGE_MONTH4

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates mobile usage statistics (including MMS, SMS, voice calls (TALE), and data usage with corresponding revenues) for a specified month. It processes detailed usage data from various sources, aggregates it by month and subscription ID, and then loads the results into a specific partition of a permanent analytical table. The loading is performed using a temporary table and an 'EXCHANGE PARTITION' operation for efficient data replacement or insertion into the partitioned target table. It also manages the existence of both the temporary table and the target table's partition.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
- ← [[GALAXY.CALL_TYPE_DIM]]
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[TMP_MOBILE_USAGE_MONTH]]
- → [[ADM_MOBILE_USAGE_MONTH_NEW2]]

