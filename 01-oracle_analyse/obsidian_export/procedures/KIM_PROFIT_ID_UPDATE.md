# KIM_PROFIT_ID_UPDATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates the PROFIT_ID column in the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table. It first initializes/cleans up specific records by setting PROFIT_ID to -2. Subsequently, it assigns profit categories to other records, where PROFIT_ID is currently -1, by matching subscription information and historical profit categories from CCDW.SUBSCRIPTION_MAPPING and PROFIT.CP_CAT_BED_PRIV using 2-month and 3-month lookback periods.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| SUBSCRIPTION_KEY |
| CONTACT_MONTH_KEY |
| PROFIT_ID |
| SOURCE_SYSTEM_KEY |
| MEASURE_TYPE |
| CONTACT_DTTM |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |
| SOURCE_SYSTEM_KEY |
- ← [[PROFIT.CP_CAT_BED_PRIV]]
| Column Name |
|---|
| SUBSCR_ID |
| PERIOD_ID |
| CATEGORY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| PROFIT_ID |

