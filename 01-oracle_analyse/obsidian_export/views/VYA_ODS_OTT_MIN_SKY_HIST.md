# VYA_ODS_OTT_MIN_SKY_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and prepares historical usage data for the 'Min Sky' (My Cloud) OTT service. It integrates user activity KPIs (foreground, connection), storage quotas, media file counts, and opt-out preferences with customer and user identifiers. This data is intended for loading into a data warehouse or analytical system.

## Data Sources (Inputs)
- ← [[CLM_ADM.SCD2_MIN_SKY_MAIN]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

