# ADM16_USER_SUBS_CNT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure creates and manages a partitioned summary table, ADM_USER_SUBS_CNT, in the CRM_ANALYSE schema. For a given month range, it checks if the target table and its specific monthly partitions exist. If the table doesn't exist, it creates it along with an initial partition and a unique index. For each month in the range, if the corresponding partition is empty or missing, it creates the partition and then inserts aggregated user subscription counts and active days (categorized by various subscription types like Mobile PostPaid, PrePaid, Mobile Broadband, Fixed-line, DSL, Fiber, and specific brands) from detailed subscription history tables into the respective monthly partition. It also includes checks for data availability in source tables and logs execution details (though the logging target table is external to this script's direct DML).

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
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| KURT_ID_USER |
| SUBS_NO_DAYS_ACTIVE |
| BUSINESS_AREA_ID |
| PRODUCT_BRAND |
- ← [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBS_TYPE |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_USER_SUBS_CNT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_USER |
| USER_NO_MPP |
| USER_NO_MPR |
| USER_NO_MBB |
| USER_NO_FIX |
| USER_NO_DSL |
| USER_NO_FBR |
| USER_NO_TNM_SUBSR |
| USER_NO_DJU_SUBSR |
| USER_MPP_NO_DAYS_ACTIVE |
| USER_MPR_NO_DAYS_ACTIVE |
| USER_MBB_NO_DAYS_ACTIVE |
| USER_FIX_NO_DAYS_ACTIVE |
| USER_DSL_NO_DAYS_ACTIVE |
| USER_FIB_NO_DAYS_ACTIVE |
| USER_NO_MPP_BUS_SUBS |
| USER_NO_MBB_BUS_SUBS |
| USER_NO_FIX_BUS_SUBS |
| USER_NO_DSL_BUS_SUBS |
| USER_NO_FBR_BUS_SUBS |
| USER_MPP_BUS_NO_DAYS_ACTIVE |
| USER_MBB_BUS_NO_DAYS_ACTIVE |
| USER_FIX_BUS_NO_DAYS_ACTIVE |
| USER_DSL_BUS_NO_DAYS_ACTIVE |
| USER_FBR_BUS_NO_DAYS_ACTIVE |

