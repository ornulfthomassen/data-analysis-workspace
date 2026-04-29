# VYA_FTV_QLIK_STOCK

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`VYA_FTV_QLIK_STOCK`) combines stock and performance metrics with detailed temporal attributes (day, week, month, year) for Qlik Sense reporting. It generates both weekly and monthly period keys from the `GALAXY.DATE_DIM_MV` for specific years (2022-2024) and then performs a `RIGHT JOIN` with `CLM_ADM.FTV_QLIK_STOCKAPP`. This ensures that all specified date periods are represented in the output, even if there's no matching stock data, and enriches these periods with various product, KPI, and churn-related metrics.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_QLIK_STOCKAPP]]
| Column Name |
|---|
| FTV_PRODUCT_KEY |
| DU_TYPE |
| PRODUCT_CATECORY |
| KPI_FLAG |
| DUALPLAY |
| CHURN_COMPANY |
| SERVICE |
| SOURCE_SYSTEM |
| SUB_PRODUCT_SK |
| VALUECHAIN |
| SUB_PRODUCT_NAME |
| SUB_PRODUCT_AREA |
| SUB_PRODUCT_REPORTING |
| TECHNOLOGY |
| SUB_PRODUCT_POID |
| TILVEKST_UTBYGGING |
| TILVEKST_ONNET |
| TILVEKST_OFFNET |
| NETTO_TEK_CROSSOVER |
| KPI_OPENING_BALANCE |
| KPI_CLOSING_BALANCE |
| CHURN_FLYTTING |
| CHURN_KONKURRENT |
| CHURN_VULA |
| CHURN |
| CHURN_ANNEN |
| UNEXPLAINED |
| MONTH_FLAG |
| WEEK_FLAG |
| PERIOD_KEY |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| "YEAR" |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
| "DAY" |
| WEEK_NUMBER |
| MONTH_NAME |
| MONTH_SHORT_NAME |
| MONTH_NUMBER |
| RELATIVE_MONTH |
| RELATIVE_WEEK |

