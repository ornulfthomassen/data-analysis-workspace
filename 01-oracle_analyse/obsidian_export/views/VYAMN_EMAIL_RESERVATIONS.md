# VYAMN_EMAIL_RESERVATIONS

**Schema:** `CCM` | **Type:** `View`

## Description
Provides email reservation data, filtered and mapped to customer keys, primarily for loading into SAS. It retrieves email reservation details, applies a filter for specific email indicators and recent dates, and attempts to link these reservations to customer keys.

## Data Sources (Inputs)
- ← [[ODS.ANA_CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| EMAIL_RA_MAX_DTTM |
| EMAIL_ADDRESS |
| CUSTOMER_ID |
| EMAIL_IND |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_KEY |
| KURT_ID |

