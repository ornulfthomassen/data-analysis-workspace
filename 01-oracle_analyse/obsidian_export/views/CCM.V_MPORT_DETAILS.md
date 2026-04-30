# V_MPORT_DETAILS

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a detailed view of mobile number porting (MNP) events by enriching base porting data from V_MPORT with customer category information from CP_CAT_BED_PRIV and historical handset usage data from KIM_HANDSET_HISTORY_V, calculating derived fields for analysis such as weekly arrival, profit month keys, and service provider groups.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.V_MPORT]]
| Column Name |
|---|
| KURT_ID_OWNER |
| KURT_ID_PAYER |
| KURT_ID_USER |
| MAIN_NUMBER |
| MARKET_AREA_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_ARRIVAL_DTTM |
| ORDER_ID |
| ORDER_STATUS_DATE |
| ORDER_STATUS_DTTM |
| ORDER_STATUS_ID |
| ORIGINAL_START_DATE |
| PARENT_SUBSCRIPTION_ID |
| PORT_DATE |
| PORT_DAYS |
| PORT_DTTM |
| PORT_WEEK |
| PORT_YEAR |
| PRODUCT_OFFER_ID |
| SERVICE_PROVIDER_ID_OUT |
| SERVICE_PROVIDER_ID_OUT_NAME |
| SOURCE_SYSTEM_KEY |
| SUBSCRIPTION_ID |

- ← [[PROFIT.CP_CAT_BED_PRIV]]
| Column Name |
|---|
| CATEGORY |
| SUBSCR_ID |
| PERIOD_ID |

- ← [[CRM_ANALYSE.KIM_HANDSET_HISTORY_V]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
| HANDSET_KEY |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |


