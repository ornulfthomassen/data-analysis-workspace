# P_ADM_MOBILE_USAGE_MONTH2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_MOBILE_USAGE_MONTH2 aggregates mobile usage data (including MMS, SMS, call 'Tale' details, data volume, and associated revenues) on a monthly basis for each subscription. It calculates various metrics, breaking them down by service type, domestic/international/roaming usage, and specific product/traffic types. The aggregated results for a given month are initially stored in a dynamically created temporary table. Subsequently, this temporary table's data is loaded into a corresponding monthly partition of a permanent analytical table using a partition exchange operation. The procedure also handles the creation of new partitions if they don't exist and cleans up the temporary table after the exchange.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]

## Target Tables (Outputs)
- → [[TMP_MOBILE_USAGE_MONTH]]
- → [[ADM_MOBILE_USAGE_MONTH_NEW]]

