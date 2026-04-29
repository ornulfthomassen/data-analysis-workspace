# VYA_ORDER_LINE_DETAIL_FACT_NB

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a detailed fact view for order lines, specifically for 'Nettbutikken' (webshop) device sales. This view includes sales that do not have existing order entries in `ORDER_LINE_DETAIL_FACT_MV`. It enriches device delivery details with dimensional data for dates and dealers, leveraging a temporary device dimension for efficient lookups.

## Data Sources (Inputs)
- ← [[CCM.VYA_INSIGHT_DEVICE_FROM_NB]]
| Column Name |
|---|
| IMEI_FULL |
| HANDSET_KEY |
| HANDSET_DELIVERED_DATE |
| HANDSET_DELIVERED_DTTM |
| IMEI_USE |
- ← [[GALAXY.DEVICE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| SOURCE_DEVICE_ID |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| IMEI |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| WEEK_NUMBER |
| RELATIVE_WEEK |
| MONTH_NUMBER |
| RELATIVE_MONTH |
| YEAR |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
| YEAR_QUARTER_NUMBER |
| DATE_KEY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| START_DT_KEY |
| END_DT_KEY |
| SOURCE_DEALER_ID |

