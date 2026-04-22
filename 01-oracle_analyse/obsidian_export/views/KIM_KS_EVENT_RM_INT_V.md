# KIM_KS_EVENT_RM_INT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_KS_EVENT_RM_INT_V`, provides a comprehensive and standardized representation of customer interaction events (likely from a 'KS' system or platform). It extracts, renames, and transforms various raw interaction attributes and metrics into a unified structure, including details about event names, descriptions, categories, groups, areas, IDs, statuses, types, objectives, timestamps, channels, products, customer and subscription IDs, device information, churn/sales indicators, interaction direction, and numerous custom metrics like durations (ACW, talk, hold, wait), counts (handle, lost, dial, ring), callback types, and customer satisfaction (CSAT) scores. It also calculates a `KPI_EVENT_DURATION` and generates a `PARTITION_SK` using a random value.

## Data Sources (Inputs)
- ← [[CCM.KIM_KS_RM_INTERACTION2_V]]

