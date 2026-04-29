# P_KIM_CAMPAIGN_DETAIL_FACT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Checks for the existence of a specific monthly partition in the 'KIM_CAMPAIGN_DETAIL_FACT' table for the upcoming month and adds it if it does not already exist. The partition is named 'CONTACT_YYYYMM' and its boundary is the first day of the month two months from now.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]

