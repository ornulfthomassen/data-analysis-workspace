# P_ADM_SUBSCR_TWIN_HIST2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBSCR_TWIN_HIST2 generates and stores historical subscription 'twin' data (e.g., related to twin SIM cards or similar subscription features) for a specified month (P_YYYYMM). It achieves this by querying and joining various subscription, product, and historical data from different source systems (CM, CCDW, GALAXY). The aggregated data is first staged in a temporary table, which is then used to populate a new partition within a permanent, partitioned historical table named ADM_SUBSCR_TWIN_HIST2. The procedure also includes checks for the availability of source data and handles error conditions.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_COMPONENT]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_TWIN_HIST2]]
- → [[TMP_SUBSCR_TWIN_HIST1_2]]

