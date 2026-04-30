# ADM_CLM_SEGMENT_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a filtered and transformed view of customer segmentation data, standardizing key identifiers (KURT_ID and PERIOD_MONTH_KEY), deriving a month-end date (PERIOD_MONTH_DATE), and creating a composite key (MONTH_KURT_KEY). The view only includes data for periods starting from December 2015.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CLM_SEGMENT_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| AGE |
| CLM_LIVSFASE |
| X_LIVSFASE |


