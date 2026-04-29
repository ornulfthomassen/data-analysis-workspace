# P_GOV_DQ_MARTS_INS_KIM_CHECK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Performs a data quality check on KIM sales data by comparing recent median daily sales against sales from two days prior. It categorizes the sales difference as 'OK' or 'WATCH' and logs this status, along with other descriptive information, into a governance data quality monitoring table.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT_V]]
| Column Name |
|---|
| KPI_SALES |
| contact_date_key |
- ← [[galaxy.date_dim_mv]]
| Column Name |
|---|
| DATE_KEY |
| day |
| type_of_day |

## Target Tables (Outputs)
- → [[CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |

