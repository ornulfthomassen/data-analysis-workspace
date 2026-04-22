# KIM_KS_RM_INTERACTION2_TELMI_V

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and enriches customer interaction data by joining core interaction records with customer demographics, survey feedback (CSAT scores), and predicted intent information. It provides a detailed, segment-level perspective of customer interactions, including various duration and count metrics, queue information, and customer-related attributes. The view is currently defined to retrieve data specifically for the period between February 1st and February 14th, 2021.

## Data Sources (Inputs)
- ← [[RSSHUGIN.RM_KS_INTERACTION]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]
- ← [[RSSHUGIN.TELMI_INTENT]]

