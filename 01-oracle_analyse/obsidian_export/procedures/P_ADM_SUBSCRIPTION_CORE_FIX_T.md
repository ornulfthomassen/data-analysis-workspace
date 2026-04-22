# P_ADM_SUBSCRIPTION_CORE_FIX_T

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_SUBSCRIPTION_CORE_FIX_T`, is designed to process and consolidate fixed telephony subscription data. Its main purpose is to cleanse, enrich, and transform raw subscription information, calculate historical relationships (e.g., previous subscriptions, days between subscriptions), and identify number portability (in-porting and out-porting) events. The processed data is then loaded into several permanent 'ADM' (presumably Administrative or Analytical Data Mart) tables, utilizing temporary 'TMP' tables for intermediate calculations and backup tables ('_BK') for data integrity during updates.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[GALAXY.DEALER_DIM]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_RAW_FIX_T]]
- → [[ADM_SUBSCRIPTION_RAW_FIX_T_BK]]
- → [[TMP_SUBSCRIPTION_CORE_FIX_T]]
- → [[TMP_SUBSCRIPTION_CORE_FIX_T_BK]]
- → [[ADM_SUBSCRIPTION_CORE_FIX_T]]
- → [[ADM_SUBSCRIPTION_CORE_FIX_T_BK]]
- → [[TMP_SUBSCR_IN_PORT_FIX_T]]
- → [[ADM_SUBSCR_IN_PORT_FIX_T]]
- → [[ADM_SUBSCR_IN_PORT_FIX_T_BK]]
- → [[TMP_SUBSCR_OUT_PORT_FIX_T]]
- → [[ADM_SUBSCR_OUT_PORT_FIX_T]]
- → [[ADM_SUBSCR_OUT_PORT_FIX_T_BK]]

