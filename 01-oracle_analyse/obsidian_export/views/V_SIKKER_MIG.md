# V_SIKKER_MIG

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies unique `agreement_id`s that are associated with two specific products: 'Sikker ID' and 'SAFE'. Specifically, it selects agreements that have a 'Sikker ID' product whose end date is between March 23, 2020, and tomorrow's date, AND simultaneously have a 'SAFE' product whose start date is on or after March 23, 2020. This likely aims to find customers or agreements that have, or have had, both these products within a specific timeframe, possibly for migration, upgrade, or bundled service analysis.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]

