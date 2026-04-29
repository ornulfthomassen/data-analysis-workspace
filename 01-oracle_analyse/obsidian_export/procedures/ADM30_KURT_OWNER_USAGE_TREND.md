# ADM30_KURT_OWNER_USAGE_TREND

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates and populates monthly usage trend metrics for subscribers/owners (`KURT_ID_OWNER`) into a partitioned summary table (`CRM_ANALYSE.ADM_KURT_OWNER_USAGE_TREND`). It manages the creation of the target table, its indexes, and monthly partitions, deriving trends from monthly aggregated subscription data and date dimension information.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
| FIRST_DATE |
| RELATIVE_MONTH |
- ← [[CRM_ANALYSE.ADM_KURT_OWNER_SUBS_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| NET_FEE |
| NET_USE |
| MPP_KR_MB_TOT_LAST1 |
| MPP_MB_TOT_LAST1 |
| MPP_SMS_DOM_LAST1 |
| MPP_VOL_VOICE_DOM_LAST1 |
| MPP_NO_VOICE_DOM_LAST1 |
| NO_MPP |
- ← [[CRM_ANALYSE.ADM_KURT_OWNER_USAGE_TREND]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_KURT_OWNER_USAGE_TREND]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
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

