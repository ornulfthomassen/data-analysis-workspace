# VYAMN_RESPONSE_STG

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'VYAMN_RESPONSE_STG', serves as a staging area to prepare and enrich campaign response data. It extracts detailed response information (like event keys, timestamps, channels, campaign details, communication specifics, and external IDs) from a primary response staging table. It enriches this data by joining with customer and subscription master data to link responses to specific customers and subscriptions. Date/time fields are broken down into week, month, and date keys, and a 'MULTI_NODE_COL' is calculated, likely for partitioning or distribution in a target system. The overall purpose is to consolidate and format response data for loading into a Customer Analytics System (CAS).

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_RESPONSE_STG]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

