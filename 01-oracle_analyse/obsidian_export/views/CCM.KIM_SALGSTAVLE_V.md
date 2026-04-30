# KIM_SALGSTAVLE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a view from the KIM_SALGSTAVLE_T table, selecting all its columns and applying a transformation to the MAIN_NUMBER column. Specifically, if MAIN_NUMBER is null or less than 1, it is set to NULL in the view; otherwise, its original value is retained.

## Data Sources (Inputs)
- ← [[CCM.KIM_SALGSTAVLE_T]]
| Column Name |
|---|
| KURT_ID_OWNER |
| MAIN_NUMBER |
| CAMPAIGN_NM |
| COMMUNICATION_TXT |
| OFFER_TXT |
| COM_ACTION_CAT |
| COM_OFFER_CAT |
| KILDE_SYSTEM |
| CHANNEL_NM |
| COMMUNICATION_DATETIME |
| RESPONSE_NM |
| RESPONSE_DATE |
| COMMUNICATION_NM |
| TREATMENT_NM |
| TREATMENT_ID |
| SORT_ORDER |


