# P_ADM_CUSTOMER_DETAIL

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure calculates and aggregates customer-specific data (e.g., subscription counts, household demographics) for a given month (`P_YYYYMM`) by joining various core and analytical customer tables. It then updates or inserts this aggregated data into a specific monthly partition of the `CLM_ADM.ADM_CUSTOMER_DETAIL` table using a 'create table as select' (CTAS) and 'exchange partition' strategy. This involves creating a temporary table, populating it with the aggregated data, and then atomically swapping it with the target partition.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CORE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
- ← [[CRM_ANALYSE.ADM_KURT_OWNER_SUBS_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| NO_MPP |
| NO_MPR |
| NO_MBB |
| NO_FIX |
| NO_DSL |
| NO_FBR |
| NO_TNM_SUBS |
| NO_DJU_SUBS |
- ← [[CRM_ANALYSE.ADM_KURT_USER_SUBS_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_USER |
| NO_MPP |
| NO_MPR |
| NO_MBB |
| NO_FIX |
| NO_DSL |
| NO_FBR |
| NO_TNM_SUBS |
| NO_DJU_SUBS |
- ← [[CRM_ANALYSE.BRING_ANALYTIC_UNIVERSE_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| X_SIST_OPPDATERT |
| X_LIVSFASE |
| X_BARN |
| X_SMAABARN |
| X_SKOLEBARN |
| X_SMAASKOLEBARN |
| X_TENAARINGSBARN |
| X_ANTALL_I_HUSSTAND |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CUSTOMER_DETAIL]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| NO_OWNER_MPP |
| NO_OWNER_MPR |
| NO_OWNER_MBB |
| NO_OWNER_FIX |
| NO_OWNER_DSL |
| NO_OWNER_FBR |
| NO_OWNER_TNM_SUBS |
| NO_OWNER_DJU_SUBS |
| NO_USER_MPP |
| NO_USER_MPR |
| NO_USER_MBB |
| NO_USER_FIX |
| NO_USER_DSL |
| NO_USER_FBR |
| NO_USER_TNM_SUBS |
| NO_USER_DJU_SUBS |
| X_SIST_OPPDATERT |
| X_LIVSFASE |
| X_BARN |
| X_SMAABARN |
| X_SKOLEBARN |
| X_SMAASKOLEBARN |
| X_TENAARINGSBARN |
| X_ANTALL_I_HUSSTAND |
- → [[CLM_ADM.ADM_CUSTOMER_DETAIL]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| NO_OWNER_MPP |
| NO_OWNER_MPR |
| NO_OWNER_MBB |
| NO_OWNER_FIX |
| NO_OWNER_DSL |
| NO_OWNER_FBR |
| NO_OWNER_TNM_SUBS |
| NO_OWNER_DJU_SUBS |
| NO_USER_MPP |
| NO_USER_MPR |
| NO_USER_MBB |
| NO_USER_FIX |
| NO_USER_DSL |
| NO_USER_FBR |
| NO_USER_TNM_SUBS |
| NO_USER_DJU_SUBS |
| X_SIST_OPPDATERT |
| X_LIVSFASE |
| X_BARN |
| X_SMAABARN |
| X_SKOLEBARN |
| X_SMAASKOLEBARN |
| X_TENAARINGSBARN |
| X_ANTALL_I_HUSSTAND |

