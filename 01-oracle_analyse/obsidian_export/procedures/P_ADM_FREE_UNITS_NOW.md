# P_ADM_FREE_UNITS_NOW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_FREE_UNITS_NOW`, processes and aggregates 'free unit' data (such as data rollover, leftover, and included units) from an operational system (OCS) and other data sources. It transforms this raw data into two main analytical tables: `ADM_FREE_UNITS_SUBS` for subscription-related free units and `ADM_FREE_UNITS_AGRM` for agreement-related free units. The procedure follows an ETL pattern, creating intermediate temporary tables, then renaming these temporary tables to become the final permanent tables, while also managing backup versions of the permanent tables.

## Data Sources (Inputs)
- ← [[OCS.OCS_FREE_UNITS]]
- ← [[PCAT.COMPONENT]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CCDW.AGREEMENT_MAPPING]]
- ← [[CM.AGREEMENT_NEW]]
- ← [[CCDW.AGREEMENT]]

## Target Tables (Outputs)
- → [[TMP_FREE_UNITS_RAW]]
- → [[TMP_FREE_UNITS_SUBS]]
- → [[ADM_FREE_UNITS_SUBS_BCK]]
- → [[ADM_FREE_UNITS_SUBS]]
- → [[TMP_FREE_UNITS_AGRM]]
- → [[ADM_FREE_UNITS_AGRM_BCK]]
- → [[ADM_FREE_UNITS_AGRM]]

