# VYA_FTV_KAS_LOC_SUB_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and pivots subscription data from `GALAXY.SUBSCRIPTION_DIM` for the 'KAS' source system, specifically extracting 'Bredbånd' (broadband) and 'TV' subscription keys and KAS customer numbers. It groups data by user location, market area, and source system, ensuring that for each combination, there is only one distinct subscription key per category. This uniqueness check is applied under two conditions: first, considering all relevant subscriptions; and second, considering only active ('A') subscriptions. The results from both conditions are combined, and the output includes separate columns for Broadband and TV subscription details.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCR_USER_LOC_KEY |
| SOURCE_SUBSCR_ID_1 |
| SUBSCRIPTION_KEY |
| MARKET_AREA_DESC |
| SUBSCR_CATEGORY_NAME |
| SOURCE_SYSTEM_NAME |
| CURRENT_STATUS |

