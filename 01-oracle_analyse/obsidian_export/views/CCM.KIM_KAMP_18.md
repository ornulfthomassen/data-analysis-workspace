# KIM_KAMP_18

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and summarizes campaign detail information, specifically for campaign 'C18' and contact dates from 2017 onwards. It joins two campaign detail fact tables, filters by campaign and date, and then groups the results by 'main_number' to find the maximum activity ID, contact date key, and activity description for each main number.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| main_number |
| activity_id |
| contact_date_key |
| contact_key |
| campaign_id |
| ACTIVITY_DESC |

- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| contact_key |


