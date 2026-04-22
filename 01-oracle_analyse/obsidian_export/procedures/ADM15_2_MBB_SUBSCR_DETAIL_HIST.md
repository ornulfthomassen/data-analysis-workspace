# ADM15_2_MBB_SUBSCR_DETAIL_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure is designed to create and/or populate a historical detail table for Mobile Broadband (MBB) subscriptions, named ADM_MBB_SUBSCR_DETAIL_HIST. It iterates through a range of months, validating the availability of source data for each month. If the target table or its partition for a given month does not exist or is empty, it dynamically creates the table (if necessary), adds the required partition, and inserts detailed subscription data by joining information from various CRM and product-related tables. It also manages indexes and gathers statistics on the table/partitions. The overall purpose is to build and maintain a structured historical record of MBB subscription details for analytical purposes.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_MBB_SUBSCR_DETAIL_HIST]]

