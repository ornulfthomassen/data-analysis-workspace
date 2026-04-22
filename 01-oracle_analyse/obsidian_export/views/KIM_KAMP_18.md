# KIM_KAMP_18

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and summarizes specific activity details for a particular campaign ('C18') from January 1, 2017, onwards. It joins campaign detail fact tables, filters by campaign ID and contact date, and then groups the results by 'main_number' to extract the maximum (latest or highest) activity ID, contact date, and activity description for each unique main number within the specified criteria.

## Data Sources (Inputs)
- ← [[crm_analyse.kim_campaign_detail_fact]]
- ← [[crm_analyse.kim_campaign_detail_fact_ext]]

