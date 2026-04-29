# FTV_SUBSCR_LOCATION_KEY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and determines the `INSTALL_LOCATION_KEY` for various subscriptions by applying a series of lookup strategies. It aims to provide a resolved installation location key, particularly for cases with missing data or specific apartment-related location assignments, using data from subscription, location, and mapping dimensions. If multiple strategies yield a location key for a subscription, the maximum value is selected.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_MISSING_FAR_ID_TMP]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| FAR_ID_INSTALL |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| END_DATE |
| SUBSCR_USER_LOC_KEY |
| USER_CUSTOMER_KEY |
| SOURCE_SYSTEM_NAME |
| SUBSCR_CATEGORY_NAME |
| MARKET_AREA_DESC |
| SUBSCR_FWA_LOC_KEY |
- ← [[CCM.FTV_MAP_APARTMENT_LOC_KEY]]
| Column Name |
|---|
| CURRENT_APARTMENT_LOC_KEY |
| LOCATION_KEY |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| IS_APARTMENT |
| ADDRESS_ID |
| CURRENT_GEOGRAPHY_ID |
| IS_CURRENT |

