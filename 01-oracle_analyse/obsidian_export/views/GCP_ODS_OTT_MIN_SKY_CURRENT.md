# GCP_ODS_OTT_MIN_SKY_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates 'Min Sky' application usage metrics, storage quotas, and user preferences at the customer level. It calculates various activity counts (foreground and connection events) over recent time periods (last 7, 30, 180 days), determines creation and last activity dates, and sums up storage quotas (total and used, converted to GB) and media file counts. The view also captures opt-out preferences for product improvement analytics and counts the number of distinct user IDs associated with each customer ID. This data is intended for loading into a data warehouse or analytical system.

## Data Sources (Inputs)
- ← [[CLM_ADM.SCD2_MIN_SKY_MAIN]]
- ← [[ODS.CONNECT_ID_LINK]]

