# V_AST_RESPONSE

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and categorizes sales tip response data from a fact table and associated dimension tables. It calculates a sum of response quantities, derives categories (e.g., KATEGORI_GR, KATEGORI, SALGSTIPS_PRODUKT_GR) from sales tip codes and response names, and filters for records where the contacted quantity is zero.

## Data Sources (Inputs)
- ← [[GALAXY.SALESTIPS_DETAIL_FACT_V]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| CUSTOMER_KEY |
| RESPONSE_QUANTITY |
| RESPONSE_DT |
| RESPONSE_KEY |
| SALESTIPS_KEY |
| CONTACTED_QUANTITY |
- ← [[GALAXY.SALESTIPS_RESPONSE_DT_DIM_V]]
| Column Name |
|---|
| SALESTIPS_RESPONSE_DT_KEY |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.SALESTIPS_RESPONSE_DIM_V]]
| Column Name |
|---|
| RESPONSE_NAME |
| RESPONSE_KEY |
- ← [[GALAXY.SALESTIPS_DIM_V]]
| Column Name |
|---|
| SALESTIPS_CODE |
| SALESTIPS_NAME |
| SALESTIPS_KEY |

