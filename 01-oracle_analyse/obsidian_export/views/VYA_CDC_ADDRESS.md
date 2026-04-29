# VYA_CDC_ADDRESS

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates address information primarily from the CDC.ADDRESS table, enriching it with 'GRUNNKRETSNUMMER' from the FAR.FARADR table based on a matching FAR_ID. It transforms the FAR_ID into a formatted string (FAR_ID_N) and filters records where FAR_ID is positive. The view seems to combine Change Data Capture (CDC) address data with additional address details from another system ('FAR').

## Data Sources (Inputs)
- ← [[CDC.ADDRESS]]
| Column Name |
|---|
| ADDRESS_TYPE_LINK_ID |
| FAR_ID |
| POSTCODE_ID |
| POSTCODE_NAME |
| ADDRESS_FORMAT_TYPE_ID |
| HOUSE_CHARACTER |
| COUNTRY_CODE |
| INFO_REG_USER_NAME |
| INFO_REG_APPL_NAME |
| INFO_REG_DATE |
| INFO_CHG_USER_NAME |
| INFO_CHG_APPL_NAME |
| INFO_CHG_DATE |
| INFO_IS_DELETED |
- ← [[FAR.FARADR]]
| Column Name |
|---|
| GRUNNKRETSNUMMER |
| ADRIDENT |

