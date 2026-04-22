# V_A162_SAFE_ONB

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the most recent (latest contact datetime) activity details for each customer, specifically for 'activity_id' A162, from March 2020 onwards. It maps customer IDs and joins campaign details with their extensions.

## Data Sources (Inputs)
- ← [[crm_analyse.kim_campaign_detail_fact]]
- ← [[crm_analyse.kim_campaign_detail_fact_ext]]
- ← [[clm_adm.adm_customer_mapping]]

