# ADM04_FIBER_FAR_COVERAGE_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Loads historical fiber far coverage data for the previous month into a permanent, partitioned administrative table (`ADM_FIBER_FAR_COVERAGE_HIST`). It uses a temporary staging table (`TMP_FIBER_FAR_COVERAGE_HIST`) to extract and prepare the data, which is then quickly integrated into the target table via a partition exchange operation. The process also handles partition creation and gathers table statistics.

## Data Sources (Inputs)
- ← [[FAR.FIBER_FAR_COVERAGE]]
| Column Name |
|---|
| FAR_ID |
| SOURCE |
| CONNECTION |
| TECHNOLOGY |
| DETAIL_1 |
| DETAIL_2 |
| CONSUMER_PROVIDER |
| BUSINESS_PROVIDER |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.TMP_FIBER_FAR_COVERAGE_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FAR_ID |
| SOURCE |
| CONNECTION |
| TECHNOLOGY |
| DETAIL_1 |
| DETAIL_2 |
| CONSUMER_PROVIDER |
| BUSINESS_PROVIDER |
- → [[CRM_ANALYSE.ADM_FIBER_FAR_COVERAGE_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FAR_ID |
| SOURCE |
| CONNECTION |
| TECHNOLOGY |
| DETAIL_1 |
| DETAIL_2 |
| CONSUMER_PROVIDER |
| BUSINESS_PROVIDER |

