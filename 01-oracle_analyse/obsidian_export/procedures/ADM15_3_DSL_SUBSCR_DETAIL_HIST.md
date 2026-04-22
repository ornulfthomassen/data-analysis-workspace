# ADM15_3_DSL_SUBSCR_DETAIL_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADM15_3_DSL_SUBSCR_DETAIL_HIST`, is designed to create and populate a partitioned historical detail table for DSL (ADSL/VDSL) internet subscriptions. It first checks for the existence of the target table `CRM_ANALYSE.ADM_DSL_SUBSCR_DETAIL_HIST`. If the table does not exist, it creates it with specific columns, partitioned by month (`PERIOD_MONTH_KEY`), and then adds local indexes. The procedure then iterates through a range of months (determined by `V_YYYYMM_FRA` and `V_YYYYMM_TIL`). For each month, it performs checks on the availability of source data and creates a new partition for the target table if one doesn't already exist for that month. Finally, it inserts detailed DSL subscription data, including product information, binding end dates, and active days, into the respective monthly partition of `CRM_ANALYSE.ADM_DSL_SUBSCR_DETAIL_HIST` by extracting and transforming data from multiple source tables. It also gathers statistics and logs the load process.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.PRODUCT_OFFER]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]

## Target Tables (Outputs)
- → [[ADM_DSL_SUBSCR_DETAIL_HIST]]

