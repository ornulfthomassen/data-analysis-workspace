# P_TRA_CHURN_FORECAST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure calculates and forecasts churn metrics. It first determines the latest period and event timestamps from a source view. It then computes various date-related statistics (days, weekdays, weekends in a period) and uses these to derive 'share' factors. Finally, it creates a temporary table containing forecasted churn KPIs by applying these share factors to the original KPI values from the source data, filtered by event timestamp. The process involves extensive logging and error handling.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_CHURN_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| EVENT_DTTM |
| subscription_key |
| event_date |
| EVENT_STATUS_DATE |
| EVENT_STATUS_DTTM |
| PERIOD_MONTH_DATE |
| SERV_PROVIDER_TO |
| ORDER_MAIN_ID_SK |
| KPI_CHURN |
| KPI_PORTING_OUTBOUND |
| KPI_PORTING_OUTBOUND_FB |
| KPI_TERMINATION |
- ← [[ALL_OBJECTS]]
| Column Name |
|---|
| OWNER |
| OBJECT_NAME |
- ← [[CLM_ADM.TMP_CP_CHURN_CALC]]
| Column Name |
|---|
| FIRST_CHURN_DATE_TO_USE |
| LAST_CHURN_DATE_TO_USE |
| MAX_CHURN_DATE_FOR_PERIOD |
- ← [[CLM_ADM.TMP_CHURN_FORECAST]]
| Column Name |
|---|
| period_month_key |
| kpi_churn |
| kpi_churn_fc |
| kpi_churn_fc2 |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CP_CHURN_CALC]]
| Column Name |
|---|
| last_midnight |
| period_start |
| max_churn_date_for_period |
| first_churn_date_to_use |
| last_churn_date_to_use |
- → [[CLM_ADM.TMP_CHURN_FORECAST]]
| Column Name |
|---|
| subscription_key |
| event_dttm |
| event_date |
| EVENT_STATUS_DATE |
| EVENT_STATUS_DTTM |
| PERIOD_MONTH_DATE |
| period_month_key |
| SERV_PROVIDER_TO |
| ORDER_MAIN_ID_SK |
| KPI_CHURN |
| KPI_PORTING_OUTBOUND |
| KPI_PORTING_OUTBOUND_FB |
| KPI_TERMINATION |
| KPI_CHURN_FC |
| KPI_PORTING_OUTBOUND_FC |
| KPI_PORTING_OUTBOUND_FB_FC |
| KPI_TERMINATION_FC |
| KPI_CHURN_FC2 |
| KPI_PORTING_OUTBOUND_FC2 |
| KPI_PORTING_OUTBOUND_FB_FC2 |
| KPI_TERMINATION_FC2 |

