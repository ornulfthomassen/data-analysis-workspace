# VYAMN_EMAIL_RESERVATIONS

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts email reservation data, including email address, reservation timestamp, and associated customer key (defaulting to 'Unknown' if not found), for loading into SAS. It filters for specific email indicators (email_ind = 2) and reservations from 2023 onwards.

## Data Sources (Inputs)
- ← [[ODS.ANA_CUSTOMER_RES_AND_APP]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

