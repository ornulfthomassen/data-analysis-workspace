# P_ADM_CLM_SEGMENT_CUSTOMER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure manages and populates the `CLM_ADM.ADM_CLM_SEGMENT_CUSTOMER` table. It ensures the table exists, creates it if necessary, and sets up its initial partitioning and indexing. For a given (or derived) range of year-months, it iterates through each month, dropping and re-adding a corresponding partition to the main table. It then inserts segmented customer and household demographic data, enriched with analytical universe information, into the appropriate monthly partitions. This process involves calculating customer lifecycle segments using a custom function.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| DATE_KEY |
| YEAR_MONTH_NUMBER |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| HOUSEHOLD_ID |
| DATE_OF_BIRTH |
| AGE |
| ANTALL_I_HUSSTAND |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| PERIOD_MONTH_KEY |
| ANTALL_I_HUSSTAND |
| MIN_AGE |
| ANT_BARN |
| ANT_UNGDOM |
- ← [[CRM_ANALYSE.V_BR_ANALYTIC_UNIVERSE_<YYYYMM>]]
| Column Name |
|---|
| KURT_ID |
| X_LIVSFASE |
| X_SKOLEBARN |
| X_BARN |
| X_SMAABARN |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CLM_SEGMENT_CUSTOMER]]
| Column Name |
|---|
| REFRESH_DATE |
| PERIOD_MONTH_KEY |
| KURT_ID |
| HOUSEHOLD_ID |
| DATE_OF_BIRTH |
| AGE |
| CU_ANTALL_I_HUSSTAND |
| HH_ANTALL_I_HUSSTAND |
| YNGST |
| ANT_BARN |
| ANT_UNGDOM |
| CLM_LIVSFASE |
| X_LIVSFASE |
| X_SKOLEBARN |
| X_BARN |
| X_SMAABARN |

