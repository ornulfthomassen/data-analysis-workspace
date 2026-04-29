# CUSTOMER_EVENTS_CHURN_2018_V

**Schema:** `CCM` | **Type:** `View`

## Description
The view `CUSTOMER_EVENTS_CHURN_2018_V` analyzes customer interaction and activity events by linking them to subsequent churn events that occurred from 2018 onwards. It enriches this data with customer segment information (MAP and LIVSFASE) and household demographic details, calculating the number of days between an event and a churn event for analytical purposes.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| KURT_ID_OWNER |
| MAIN_NUMBER |
| EVENT_DATE |
| EVENT_MONTH_TXT |
| EVENT |
| EVENT_CHANNEL |
| EVENT_TYPE |
| EVENT_CATEGORY |
| PROGRAM |
| ACTIVITY_ID |
| ACTIVITY_DESC |
| CAMPAIGN |
| CAMPAIGN_DESC |
| SALES_MATRIX |
| GROSS_AMOUNT_LAST_MONTH |
| HANDLE_COUNT |
| KPI_CALL_COMPLETED |
| VOLUME |
| CLOSE_CAMP_DAYS |
| CLOSE_CALL_DAYS |
| GROSS_AMOUNT |
| SOURCE_ID |
| CLOSE_CHURN_DAYS |
| ADDITIONAL_FEES |
| DATAVOLUME |
| NUM_OF_EVENTS |
| ACTIVITY_MAIN_OBJECTIVE |
- ← [[CLM_KIM.MAP_SEGMENT_TMP]]
| Column Name |
|---|
| KURT_ID |
| START_DATE |
| END_DATE |
| SEGMENT_NAME |
- ← [[CLM_KIM.LIVSFASE_CLM_TMP]]
| Column Name |
|---|
| KURT_ID |
| START_DATE |
| END_DATE |
| SEGMENT_NAME |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| AGE |
| GENDER |
| ANTALL_I_HUSSTAND |
| ADRESSE |
| POSTNR |
| POSTSTED |
| KOMMUNENR |
| GRUNNKRETS_NR |
| GRUNNKRETS |
| MOBIL_TALE |

