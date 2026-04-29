# GCP_ORDER_CUSTOMER_MAPPING_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, GCP_ORDER_CUSTOMER_MAPPING_HIST, provides a historical record of order and customer mapping information. It selects all relevant columns from the source table, performing data type casting and trimming operations on specific identifier and key columns (like ORDER_LINE_ID, ORDER_KEY, SUBSCRIPTION_SK, AGREEMENT_SK) to standardize their formats.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ORDER_CUSTOMER_MAPPING_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| ORDER_LINE_ID |
| ORDER_KEY |
| ORDER_LINE_KEY |
| SUBSCRIPTION_SK |
| AGREEMENT_SK |
| SRC_AGREEMENT_OFFER_SK |
| ORDER_DATE_KEY |
| ORDER_DATE_SK |
| SOURCE_ORDERING_ID |
| SOURCE_ORDER_ID |
| SOURCE_SYSTEM_KEY |
| OWNER_CUSTOMER_KEY |
| OWNER_CUSTOMER_SK |
| OWNER_AGE |
| OWNER_POSTADR_POSTNR |
| OWNER_POSTNR |
| OWNER_KOMMUNENR |
| OWNER_GRUNNKRETS_NR |
| USER_CUSTOMER_KEY |
| USER_CUSTOMER_SK |
| USER_AGE |
| USER_POSTADR_POSTNR |
| USER_POSTNR |
| USER_KOMMUNENR |
| USER_GRUNNKRETS_NR |
| SUBSCR_USER_LOC_KEY |
| MAIN_NUMBER_SK |
| SUBSCRIPTION_START_DATE |
| MAIN_NUMBER_START_DATE |

