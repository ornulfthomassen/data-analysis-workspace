# V_SIKKER_ROT

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies unique agreement IDs that are associated with two specific product types simultaneously. It selects agreements for the 'Sikker ID' product that have an end date within a specific period (from March 23, 2020, up to the current date) AND also have an association with the 'SAFE' product, where the 'SAFE' product's start date is on or after March 23, 2020. The purpose, as indicated by the comment, is to provide foundational data for a 'SAFE dashboard' used by a 'safe and secure squad'.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]

