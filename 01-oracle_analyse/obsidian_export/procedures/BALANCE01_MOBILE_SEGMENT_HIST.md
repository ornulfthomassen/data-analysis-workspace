# BALANCE01_MOBILE_SEGMENT_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `BALANCE01_MOBILE_SEGMENT_HIST`, populates a historical balance and segmentation table for mobile subscriptions. It processes data on a monthly basis, dynamically creating partitions in the target table as needed. The procedure integrates subscription details, product information, porting events, and various customer segmentation attributes (profit, VAR, churn, lifecycle, MAP2) from multiple source systems. It uses intermediate tables to prepare data before inserting the final, aggregated, and segmented records into the main historical table. The goal is to maintain a comprehensive historical view of mobile subscriber segments and related information.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRIMARY_PRODUCT_DIM_V]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[PROFIT.CP_CAT_PRIV]]
- ← [[crm_analyse.PROFITSEGMENT_MOBILE]]
- ← [[crm_analyse.VARSEGMENT_MOBILE]]
- ← [[crm_analyse.CHURNSEGMENT_MOBILE]]
- ← [[ADM_MOBIL_SUBSCR_HIST]]
- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[CLM_ADM.BALANCE_MOBILE_SEGMENT_HIST]]
- → [[CLM_ADM.NRPORT_PORTERINGER_M_MV]]
- → [[CLM_ADM.SUBSCRIPTION_BALANCE_RAW_M_MV]]

