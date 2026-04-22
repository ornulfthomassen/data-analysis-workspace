# KIM_MAX_CONTACT_KEY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view determines the maximum `CONTACT_KEY` from the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table. It includes a mechanism to return `0` as the maximum `CONTACT_KEY` if the `KIM_CAMPAIGN_DETAIL_FACT` table is empty, preventing a `NULL` result in such cases.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[DUAL]]

