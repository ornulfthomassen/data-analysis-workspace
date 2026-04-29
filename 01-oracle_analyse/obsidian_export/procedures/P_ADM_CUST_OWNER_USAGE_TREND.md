# P_ADM_CUST_OWNER_USAGE_TREND

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure calculates customer owner usage trends for a given month (P_YYYYMM) by aggregating data from customer subscription and month dimension tables over a 7-month period. It creates a temporary table to store these trends and then uses an 'EXCHANGE PARTITION' operation to move the data into a specific partition of the permanent 'ADM_CUSTOMER_OWNER_USAGE_TREND' table. The procedure includes checks for source data availability, existing partitions, and handles errors with logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DAY |
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_OWNER |
| NET_FEE |
| NET_USE |
| MPP_KR_MB_TOT_LAST1 |
| MPP_MB_TOT_LAST1 |
| MPP_SMS_DOM_LAST1 |
| MPP_VOL_VOICE_DOM_LAST1 |
| MPP_NO_VOICE_DOM_LAST1 |
| NO_MPP |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| FIRST_DATE |
| RELATIVE_MONTH |
- ← [[ADM_CUSTOMER_OWNER_USAGE_TREND]]
- ← [[TMP_CUSTOMER_OWNER_USAGE_TREND]]

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_OWNER_USAGE_TREND]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_OWNER |
| NO_ACTIVE_MONTHS |
| TREND_MPP_NET_FEE |
| TREND_MPP_NET_USE |
| TREND_MPP_KR_MB |
| TREND_MPP_MB |
| TREND_MPP_SMS |
| TREND_MPP_VOL_VOICE |
| TREND_MPP_NO_VOICE |
| TREND_MPP_NET_FEE_ADJ |
| TREND_MPP_NET_USE_ADJ |
| TREND_MPP_KR_MB_ADJ |
| TREND_MPP_MB_ADJ |
| TREND_MPP_SMS_ADJ |
| TREND_MPP_VOL_VOICE_ADJ |
| TREND_MPP_NO_VOICE_ADJ |
| FIRST_NO_MPP |
| LAST_NO_MPP |
| MIN_NO_MPP |
| MAX_NO_MPP |
| MEAN_NO_MPP |
- → [[ADM_CUSTOMER_OWNER_USAGE_TREND]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_OWNER |
| NO_ACTIVE_MONTHS |
| TREND_MPP_NET_FEE |
| TREND_MPP_NET_USE |
| TREND_MPP_KR_MB |
| TREND_MPP_MB |
| TREND_MPP_SMS |
| TREND_MPP_VOL_VOICE |
| TREND_MPP_NO_VOICE |
| TREND_MPP_NET_FEE_ADJ |
| TREND_MPP_NET_USE_ADJ |
| TREND_MPP_KR_MB_ADJ |
| TREND_MPP_MB_ADJ |
| TREND_MPP_SMS_ADJ |
| TREND_MPP_VOL_VOICE_ADJ |
| TREND_MPP_NO_VOICE_ADJ |
| FIRST_NO_MPP |
| LAST_NO_MPP |
| MIN_NO_MPP |
| MAX_NO_MPP |
| MEAN_NO_MPP |

