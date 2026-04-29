# TEST_PROC

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure dynamically creates a permanent table named 'TMP_SLETT_MEG' (derived from the variable V_TABLE_USE_R). This new table stores aggregated mobile roaming usage data for a specific period (February 2016) and selected market areas (2, 3, 4). It calculates the sum of net amount and net discount amount per subscription.

## Data Sources (Inputs)
- ← [[CCDW_USAGE.MOBILE_ROAMING_DAILY]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| NET_AMOUNT |
| NET_DISCOUNT_AMOUNT |
| EVENT_DATE |
| MARKET_AREA_ID |

## Target Tables (Outputs)
- → [[TMP_SLETT_MEG]]
| Column Name |
|---|
| PERIOD_ID |
| SUBSCRIPTION_ID |
| NET_AMOUNT_USE_ROAM |
| NET_DISCOUNT_AMOUNT_USE_ROAM |

