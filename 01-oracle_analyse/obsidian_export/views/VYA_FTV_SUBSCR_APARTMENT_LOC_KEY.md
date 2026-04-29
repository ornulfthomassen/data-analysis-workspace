# VYA_FTV_SUBSCR_APARTMENT_LOC_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
Filters subscriptions for specific source and category ('KAS', 'Bredbånd') from the `SUBSCRIPTION_DIM` table, joins them with `LOCATION_DIM`, and identifies `SUBSCRIPTION_KEY`s that are associated with a non-apartment location but belong to a customer and address where a unique apartment location also exists. It then returns the `SUBSCRIPTION_KEY` and that unique `APARTMENT_LOCATION_KEY`.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| SUBSCR_USER_LOC_KEY |
| USER_CUSTOMER_KEY |
| SOURCE_SYSTEM_NAME |
| SUBSCR_CATEGORY_NAME |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| ADDRESS_ID |
| IS_CURRENT |
| IS_APARTMENT |

