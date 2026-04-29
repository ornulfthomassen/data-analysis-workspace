# CUSTOMER_RES_AND_APP_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a unified view of customer reservation and application SMS data, combining it with customer mapping information. It derives key performance indicator (KPI) flags for SMS reservation and acceptance based on the SMS indicator, and filters out records with invalid SMS indicator values.

## Data Sources (Inputs)
- ← [[ODS.ANA_CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| SMS_RA_MAX_DTTM |
| CUSTOMER_ID |
| SMS_NUMBER |
| SMS_IND |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

