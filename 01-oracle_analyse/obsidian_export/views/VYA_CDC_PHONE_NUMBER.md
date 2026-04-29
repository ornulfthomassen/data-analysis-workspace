# VYA_CDC_PHONE_NUMBER

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a view by joining phone number change data capture (CDC) records with subscription master history. It enriches the natural part of the phone number by concatenating a Luhn control digit and its length, and filters/links records based on phone number and date ranges.

## Data Sources (Inputs)
- ← [[CDC.PHONE_NUMBER]]
| Column Name |
|---|
| ADDRESS_TYPE_LINK_ID |
| PHONE_NUMBER_TYPE_ID |
| PHONE_NBR_INT_PREFIX |
| PHONE_NBR_NAT_PART |
| INFO_REG_USER_NAME |
| INFO_REG_APPL_NAME |
| INFO_REG_DATE |
| INFO_CHG_USER_NAME |
| INFO_CHG_APPL_NAME |
| INFO_CHG_DATE |
| INFO_IS_DELETED |
| INFO_TRACKING_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER_SK |
| MAIN_NUMBER |
| ORIGINAL_START_DATE |
| END_DATE |

