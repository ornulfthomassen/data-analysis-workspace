# KS_INTERACTION_VIYA

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named KS_INTERACTION_VIYA, provides a consolidated and enriched dataset of customer interactions from the CRM system. It combines detailed interaction records with customer and subscription master data. The view includes a wide range of interaction-related attributes (e.g., duration, type, queue, agent info) and links them to customer and subscription identifiers. The data is filtered to only include interactions from the current day onwards (`START_CAL_DATE >= TRUNC(SYSDATE)`), suggesting it's primarily for real-time or daily analysis of recent customer interactions, potentially for a 'Viya' specific reporting or analytical tool based on the view name.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KS_INTERACTION]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

