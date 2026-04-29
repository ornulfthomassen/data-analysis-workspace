# VYA_FTV_MISSING_FAR_ID

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies and consolidates installation location keys and apartment status for 'Fixed and TV' (FTV) subscriptions. It integrates data from a temporary missing FAR_ID table, a subscription dimension, and the KAS customer/address system, prioritizing apartment-specific location details where available to provide a refined installation location.

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
| SOURCE_SUBSCR_ID_1 |
| SOURCE_SYSTEM_NAME |
| MARKET_AREA_DESC |
| SUBSCR_CATEGORY_NAME |
- ← [[CCM.FTV_MAP_APARTMENT_LOC_KEY]]
| Column Name |
|---|
| CURRENT_APARTMENT_LOC_KEY |
| IS_APARTMENT |
| LOCATION_KEY |
- ← [[KAS.KUNDE]]
| Column Name |
|---|
| ABONNENT_NR |
| ADRESSE_NR |
| NOTAT2 |
- ← [[KAS.ADRESSER]]
| Column Name |
|---|
| ADRESSE_NR |
| FAR_ID |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| IS_APARTMENT |
| GEOGRAPHY_ID_HOUSE |
| APPARTMENT_NUMBER |

