# VYA_MONTH_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates an enhanced month dimension, providing comprehensive information about each month. For each month, it includes its key attributes (e.g., first/last dates, total days, working days), and it also incorporates the same key attributes for the *next* month and the *previous six* months. It joins different instances of the `ADM_MONTH_DIM_V` view to enrich the data from `ADM_MONTH_DIM` with character-based month representations for the current, next, and previous months. This structure is particularly useful for reporting and analytical purposes that require quick access to historical and future monthly context within a single record.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]

