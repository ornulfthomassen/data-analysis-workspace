# ADM15_1_SUBSCR_DETAIL_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure `ADM15_1_SUBSCR_DETAIL_HIST` creates and populates a historical subscription detail table (`CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST`). It processes data on a month-by-month basis, dynamically creating new partitions for each month if they don't exist. For each period, it inserts detailed subscription-related metrics, such as active days for various product types (e.g., 'FRIFAM', 'FORSIK', 'MIN SKY', 'BINDING', 'DATAKONTROLL'), aggregated from multiple source systems. The procedure also manages indexes on the target table, creating them if the table is newly created, and potentially dropping/recreating them during the load process.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CRM_ANALYSE.ADM_MAIN_NUMBER_BANKID]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]

