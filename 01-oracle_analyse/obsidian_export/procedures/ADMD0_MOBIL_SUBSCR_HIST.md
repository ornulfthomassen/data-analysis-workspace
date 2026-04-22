# ADMD0_MOBIL_SUBSCR_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `ADMD0_MOBIL_SUBSCR_HIST`, constructs a detailed historical view of mobile subscriptions. It does this by creating several permanent tables: a raw subscription history table, tables for inbound and outbound porting events, a dealer-related table, and a final consolidated mobile subscription history table. The final table combines data from all intermediate tables, enriching it with product and dealer details, and categorizing subscription changes like ownership transfers or new sales, as well as porting activities.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

## Target Tables (Outputs)
- → [[ADM_MOBIL_SUBSCR_HIST_RAW]]
- → [[ADM_SUBSCR_IN_PORT]]
- → [[ADM_SUBSCR_OUT_PORT]]
- → [[ADM_DEALER_START]]
- → [[ADM_MOBIL_SUBSCR_HIST]]

