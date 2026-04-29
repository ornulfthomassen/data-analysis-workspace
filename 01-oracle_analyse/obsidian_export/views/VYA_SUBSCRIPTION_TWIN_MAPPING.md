# VYA_SUBSCRIPTION_TWIN_MAPPING

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and aggregates subscription data for 'twin' or related subscriptions (where a subscription has a different parent subscription ID). It filters by specific business and market areas, an end date range, consolidates the earliest start date and latest end date within each group, and includes the associated product name.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| parent_subscription_id |
| subscription_id |
| main_number |
| start_date |
| end_date |
| product_offer_id |
| business_area_id |
| market_Area_id |
- ← [[PD]]
| Column Name |
|---|
| product_name |
| product_key |

