# ADM12_SUBSCR_TWIN_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Populates a partitioned historical table (`CRM_ANALYSE.ADM_SUBSCR_TWIN_HIST`) with monthly data regarding mobile subscriptions linked to 'twin' cards or data cards, including associated handset and terminal details. It retrieves this data by joining various data warehouse and operational history sources, creating partitions for each month if they don't exist, and managing indexes for performance.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_TWIN_HIST]]

