# KIM_CONTACT_VS_RESPONSE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates campaign contact details and customer response details, providing the minimum date, maximum date, and total count for each 'SOURCE_SYSTEM_KEY', with a flag ('F' for contact, 'R' for response) to distinguish between the two data types.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| CONTACT_DTTM |
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| RESPONSE_DTTM |

