# VYA_ORDER_LINE_DETAIL_FACT_NB2

**Schema:** `CCM` | **Type:** `View`

## Description
This view generates order line detail fact records for new device sales originating from the 'Nettbutikken' (online store) that are not already present in the main `ORDER_LINE_DETAIL_FACT_MV` table. It populates these records with specific device, date, and dealer information, assigning default or literal values to many columns, and setting certain key performance indicators (KPIs) to indicate a new device sale or gross sale.

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

