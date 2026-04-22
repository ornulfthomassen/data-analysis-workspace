# CUSTOMER_EVENTS_CHURN_2018_V

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes customer events by identifying subsequent churn events (specifically from 2018 onwards), calculating the duration until churn, and enriching these events with demographic and customer segmentation data. It provides a comprehensive view for understanding customer behavior leading up to churn.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
- ← [[CLM_KIM.MAP_SEGMENT_TMP]]
- ← [[CLM_KIM.LIVSFASE_CLM_TMP]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]

