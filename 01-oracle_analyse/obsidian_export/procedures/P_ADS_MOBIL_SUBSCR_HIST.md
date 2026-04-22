# P_ADS_MOBIL_SUBSCR_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Constructs a comprehensive historical view of mobile subscriptions by extracting, transforming, and integrating data from raw subscription records, product dimensions, dealer information, and number porting logs. It processes data through several staging tables to enrich subscription history with previous/next states, market area changes, and reasons for subscription start/end, culminating in a detailed historical subscription analysis table.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADS_MOBIL_SUBSCR_HIST_RAW]]
- → [[CLM_ADM.ADS_SUBSCR_IN_PORT]]
- → [[CLM_ADM.ADS_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADS_DEALER_START]]
- → [[CLM_ADM.ADS_MOBIL_SUBSCR_HIST]]
- → [[CLM_ADM.TDS_MOBIL_SUBSCR_HIST]]

