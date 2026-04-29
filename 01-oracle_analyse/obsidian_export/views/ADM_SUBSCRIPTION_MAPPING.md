# ADM_SUBSCRIPTION_MAPPING

**Schema:** `CCM` | **Type:** `View`

## Description
This view, ADM_SUBSCRIPTION_MAPPING, provides a transformed and re-aliased representation of historical subscription master data, including details like subscription IDs, main numbers, parent subscriptions, start/end dates (with derived date keys), subscription type, and various historical and market area identifiers. It also includes port-in and port-out details.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| MAIN_NUMBER_SK |
| MAIN_NUMBER_RANK |
| SUBSCR_ID_NUM |
| LAST_PARENT_SUBSCRIPTION_ID |
| ORIGINAL_START_DATE |
| END_DATE |
| SUBSCR_TYPE |
| SUBSCRIPTION_ID_PREV |
| SUBSCRIPTION_ID_ORIG |
| SUBSCRIPTION_ID_PAST |
| DAYS_BETWEEN_SUBSCRIPTIONS |
| SUBSCRIPTION_ID_PAST_ORIG |
| MARKET_AREA_ID |
| MARKET_AREA_ID_PREV |
| MARKET_AREA_ID_ORIG |
| MARKET_AREA_ID_PAST |
| MARKET_AREA_ID_PAST_ORIG |
| SUBSCR_START_REASON |
| PORT_IN_DATE |
| PORT_IN_DEALER_ID |
| PORT_IN_SERV_PROV_ID |
| PORT_OUT_DATE |
| PORT_OUT_DEALER_ID |
| PORT_OUT_SERV_PROV_ID |

