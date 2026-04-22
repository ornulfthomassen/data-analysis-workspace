# P_ADM_SWAP_AGREEMENT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_SWAP_AGREEMENT` procedure processes and aggregates 'SWAP Agreement' data for a specified month (`P_YYYYMM`). It consolidates detailed information from various CRM, agreement management, product, and subscription-related data sources. The transformed data is staged in a temporary table (`TMP_ADM_SWAP_AGREEMENT`), which is then used to update or create a monthly partition within the permanent `ADM_SWAP_AGREEMENT` table via a partition exchange operation. This ensures an efficient and isolated data load for the partitioned historical data.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[LIVE.EUREKA_IMEI]]

## Target Tables (Outputs)
- → [[TMP_ADM_SWAP_AGREEMENT]]
- → [[ADM_SWAP_AGREEMENT]]

