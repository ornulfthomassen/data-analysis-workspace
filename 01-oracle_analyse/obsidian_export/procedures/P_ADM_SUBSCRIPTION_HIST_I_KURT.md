# P_ADM_SUBSCRIPTION_HIST_I_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBSCRIPTION_HIST_I_KURT calculates and stores subscription history data for the previous month (V_YYYYMM). It first validates the readiness of source data by checking the presence and freshness of records in GALAXY.DATE_DIM_MV, CRM_ANALYSE.TDM_MOBIL_SUBSCR_HIST, and ADM_SUBSCRIPTION_HIST_KURT. If data validation passes, it proceeds to create a new version of the main history table, ADM_SUBSCRIPTION_HIST_I_KURT. This involves several steps: backing up the existing ADM_SUBSCRIPTION_HIST_I_KURT table to ADM_SUBSCRIPTION_HIST_I_KURT_O, creating two temporary tables (TMP1_SUBSCRIPTION_HIST_I_KURT and TMP2_SUBSCRIPTION_HIST_I_KURT) through a series of joins and filters, and finally populating the new ADM_SUBSCRIPTION_HIST_I_KURT table by selecting the latest subscription keys from the processed temporary data. The procedure uses dynamic SQL for table creation, indexing, and statistics gathering, and logs its operational status and any errors to an administrative history table.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CRM_ANALYSE.TDM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| START_DATE |
| MARKET_AREA_ID |
| END_DATE |
- ← [[ADM_SUBSCRIPTION_HIST_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| MARKET_AREA_ID |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE |
| LAST_DATE |
- ← [[ADM_SUBSCRIPTION_HIST_I_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[TMP1_SUBSCRIPTION_HIST_I_KURT]]
- ← [[TMP2_SUBSCRIPTION_HIST_I_KURT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY_NEXT |
| MAIN_NUMBER |

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_HIST_I_KURT_O]]
- → [[TMP1_SUBSCRIPTION_HIST_I_KURT]]
- → [[TMP2_SUBSCRIPTION_HIST_I_KURT]]
- → [[ADM_SUBSCRIPTION_HIST_I_KURT]]
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TARGET_TABLE_NAME |
| PERIOD_MONTH_KEY |
| STATUS |
| MESSAGE |

