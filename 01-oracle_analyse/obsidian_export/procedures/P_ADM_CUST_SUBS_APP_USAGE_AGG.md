# P_ADM_CUST_SUBS_APP_USAGE_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_CUST_SUBS_APP_USAGE_AGG`, aggregates customer subscription and application usage data for a specified month (`P_YYYYMM`). It begins by validating the availability and quantity of source data. If the data checks pass, it ensures that a partition for the given month exists in the permanent target table (`ADM_CUST_SUBS_APP_USAGE_AGG`), creating it if necessary. Subsequently, it populates a temporary table (`TMP_CUST_SUBS_APP_USAGE_AGG`) with detailed aggregated usage metrics derived from various customer event and dimension tables. Finally, it efficiently loads this aggregated data into the corresponding partition of the permanent target table using an `ALTER TABLE ... EXCHANGE PARTITION` operation, followed by gathering statistics. The procedure includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[ADM_CUST_SUBS_APP_USAGE_AGG]]
- → [[TMP_CUST_SUBS_APP_USAGE_AGG]]

