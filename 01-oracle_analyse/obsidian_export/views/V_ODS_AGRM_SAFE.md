# V_ODS_AGRM_SAFE

**Schema:** `CCM` | **Type:** `View`

## Description
This view retrieves comprehensive details for agreements related to 'SAFE' or 'Sikker ID' products. It combines agreement general information, agreement offer specifics, and customer mapping data. The view includes agreement and product statuses, start/end dates (truncated to day), and flags indicating whether the agreement or product is currently active. It links agreements to customer surrogate keys via an internal identifier (kurt_id).

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]
- ← [[clm_adm.adm_customer_mapping]]

