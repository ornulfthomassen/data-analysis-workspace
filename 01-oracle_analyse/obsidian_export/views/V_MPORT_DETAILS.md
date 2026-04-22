# V_MPORT_DETAILS

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and enriches mobile porting (mport) details. It combines core porting transaction data from `V_MPORT` with profit-related categories from `CP_CAT_BED_PRIV` (linked by source system key and a calculated previous month) and handset usage history from `KIM_HANDSET_HISTORY_V` (linked by subscription ID and order arrival date within the handset's usage period). It also derives additional date attributes (like order arrival week, profit month link key) and categorizes service providers based on their names, providing a comprehensive dataset for analytical purposes related to mobile porting, profit, and associated handsets.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.V_MPORT]]
- ← [[PROFIT.CP_CAT_BED_PRIV]]
- ← [[CRM_ANALYSE.KIM_HANDSET_HISTORY_V]]

