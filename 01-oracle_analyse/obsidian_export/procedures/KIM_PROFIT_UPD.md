# KIM_PROFIT_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates the `PROFIT_ID` column in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table based on corresponding `SEGMENT_ID`, `SUBSCRIPTION_KEY`, and `CONTACT_MONTH_KEY` values retrieved from the `KIM_PROFIT_SEGMENT_HIST_V` view, performing batch commits.

## Data Sources (Inputs)
- ← [[KIM_PROFIT_SEGMENT_HIST_V]]
| Column Name |
|---|
| SEGMENT_ID |
| SUBSCRIPTION_KEY |
| CONTACT_MONTH_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| CONTACT_MONTH_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| PROFIT_ID |

