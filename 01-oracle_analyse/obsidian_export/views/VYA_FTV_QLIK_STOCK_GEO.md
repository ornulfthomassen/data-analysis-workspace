# VYA_FTV_QLIK_STOCK_GEO

**Schema:** `CCM` | **Type:** `View`

## Description
Combines financial/telecom stock (customer base or product inventory) data with detailed weekly and monthly time dimensions for specific years (2022-2024). It prepares a comprehensive dataset, likely for Qlik reporting, including various product/service attributes, KPIs, growth, and churn metrics, linked to calendar periods. The view leverages a right join to ensure all defined time periods are present, even if corresponding stock data is not available.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_QLIK_STOCKAPP_GEO]]
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
| MUNICIPALITY_CODE |
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
| MONTH_FLAG |
| WEEK_FLAG |
| PERIOD_KEY |
| PERIOD_END_KEY |
| DAY |
| WEEK_NUMBER |
| YEAR_WEEK_NUMBER |
| MONTH_NAME |
| MONTH_SHORT_NAME |
| MONTH_NUMBER |
| YEAR_MONTH_NUMBER |
| YEAR |
| RELATIVE_MONTH |
| RELATIVE_WEEK |
| DATE_KEY |

