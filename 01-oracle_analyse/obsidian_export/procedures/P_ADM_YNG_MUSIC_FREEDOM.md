# P_ADM_YNG_MUSIC_FREEDOM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates aggregated mobile traffic data ('MB_MUSIC_FREEDOM') for a specified month and APN, linking it to subscription details. This aggregated data is then loaded into a monthly partitioned table `ADM_YNG_MUSIC_FREEDOM` via a temporary table and partition exchange, after performing checks for source data availability and existing partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCR_ID |
| SUM_MB |
| APN |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_ID |
| INFO_REG_DATE |
| SOURCE_SYSTEM_KEY |
| SUBSCRIPTION_ID |

## Target Tables (Outputs)
- → [[TMP_YNG_MUSIC_FREEDOM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| MB_MUSIC_FREEDOM |
- → [[ADM_YNG_MUSIC_FREEDOM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| MB_MUSIC_FREEDOM |

