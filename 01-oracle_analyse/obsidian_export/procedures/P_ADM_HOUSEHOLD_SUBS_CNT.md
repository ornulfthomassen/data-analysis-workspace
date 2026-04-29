# P_ADM_HOUSEHOLD_SUBS_CNT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_HOUSEHOLD_SUBS_CNT calculates aggregated subscription counts and activity metrics at the household level for a specified month (`P_YYYYMM`). It first validates the availability of source data. Then, it manages partitioning for the permanent target table `ADM_HOUSEHOLD_SUBS_CNT`, adding a new partition if it doesn't exist for the target month. It populates a temporary table (`TMP_HOUSEHOLD_SUBS_CNT`) with the computed household-level metrics by joining various customer and subscription history tables. Finally, it uses an `EXCHANGE PARTITION` operation to replace the corresponding partition in the `ADM_HOUSEHOLD_SUBS_CNT` table with the data from the temporary table, ensuring atomic update of the historical data.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_USER |
| SUBSCRIPTION_ID |
| BUSINESS_AREA_ID |
| PRODUCT_BRAND |
| SUBS_NO_DAYS_ACTIVE |
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBS_TYPE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MB_TOT_PREV1 |
| NUMBER_OF_MMS_NORGE_PREV1 |
| NUMBER_OF_SMS_NORGE_PREV1 |
| NUMBER_OF_SMS_UTLAND_PREV1 |
| NUMBER_SPEECH_NORGE_PREV1 |
| NUMBER_SPEECH_UTLAND_PREV1 |

## Target Tables (Outputs)
- → [[TMP_HOUSEHOLD_SUBS_CNT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HH_NO_MPP_USR |
| HH_NO_MPR_USR |
| HH_NO_MPR_USR_ACTIVE |
| HH_NO_MBB_USR |
| HH_NO_FIX_USR |
| HH_NO_DSL_USR |
| HH_NO_FBR_USR |
| HH_NO_TNM_SUBSR_USR |
| HH_NO_DJU_SUBSR_USR |
| HH_MPP_NO_DAYS_ACTIVE |
| HH_MPR_NO_DAYS_ACTIVE |
| HH_MBB_NO_DAYS_ACTIVE |
| HH_FIX_NO_DAYS_ACTIVE |
| HH_DSL_NO_DAYS_ACTIVE |
| HH_FIB_NO_DAYS_ACTIVE |
| HH_NO_MPP_BUS_SUBS_USR |
| HH_NO_MBB_BUS_SUBS_USR |
| HH_NO_FIX_BUS_SUBS_USR |
| HH_NO_DSL_BUS_SUBS_USR |
| HH_NO_FBR_BUS_SUBS_USR |
| HH_MPP_BUS_NO_DAYS_ACTIVE |
| HH_MBB_BUS_NO_DAYS_ACTIVE |
| HH_FIX_BUS_NO_DAYS_ACTIVE |
| HH_DSL_BUS_NO_DAYS_ACTIVE |
| HH_FBR_BUS_NO_DAYS_ACTIVE |
- → [[ADM_HOUSEHOLD_SUBS_CNT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HH_NO_MPP_USR |
| HH_NO_MPR_USR |
| HH_NO_MPR_USR_ACTIVE |
| HH_NO_MBB_USR |
| HH_NO_FIX_USR |
| HH_NO_DSL_USR |
| HH_NO_FBR_USR |
| HH_NO_TNM_SUBSR_USR |
| HH_NO_DJU_SUBSR_USR |
| HH_MPP_NO_DAYS_ACTIVE |
| HH_MPR_NO_DAYS_ACTIVE |
| HH_MBB_NO_DAYS_ACTIVE |
| HH_FIX_NO_DAYS_ACTIVE |
| HH_DSL_NO_DAYS_ACTIVE |
| HH_FIB_NO_DAYS_ACTIVE |
| HH_NO_MPP_BUS_SUBS_USR |
| HH_NO_MBB_BUS_SUBS_USR |
| HH_NO_FIX_BUS_SUBS_USR |
| HH_NO_DSL_BUS_SUBS_USR |
| HH_NO_FBR_BUS_SUBS_USR |
| HH_MPP_BUS_NO_DAYS_ACTIVE |
| HH_MBB_BUS_NO_DAYS_ACTIVE |
| HH_FIX_BUS_NO_DAYS_ACTIVE |
| HH_DSL_BUS_NO_DAYS_ACTIVE |
| HH_FBR_BUS_NO_DAYS_ACTIVE |

