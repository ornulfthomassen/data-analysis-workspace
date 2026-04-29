# VYA_USAGE_MONTH_IMEI

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a summarized monthly usage data set, specifically focusing on IMEI-related usage. It derives the first and last days of the month from a period key and formats the subscription SIM card type. The view consolidates various usage metrics and identifiers from a temporary staging table.

## Data Sources (Inputs)
- ← [[tmp_VYA_USAGE_month_imei]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| SUB_NUMBER |
| SUBSCRIPTION_SIMCARD_TYPE |
| PRIM_PRODUCT_KEY |
| DISCOUNT_PRODUCT_OFFER_KEY |
| DESTINATION_COUNTRY_KEY |
| ROAMING_COUNTRY_KEY |
| CALL_TYPE_KEY |
| NETWORK_OPERATOR_KEY |
| TRAFFIC_TYPE_KEY |
| TWIN_SWITCH_KEY |
| IMEI |
| IMEI_HASH |
| USAGE_NUMBER_OF_EVENTS |
| USAGE_NUMBER_OF_CDR |

