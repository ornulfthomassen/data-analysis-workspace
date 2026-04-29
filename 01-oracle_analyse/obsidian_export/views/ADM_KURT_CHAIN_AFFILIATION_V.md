# ADM_KURT_CHAIN_AFFILIATION_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and transforms customer-dealer affiliation data and various Key Performance Indicators (KPIs) from the base `ADM_KURT_CHAIN_AFFILIATION` table. It standardizes data types, concatenates `PERIOD_MONTH_KEY` and `CUSTOMER_SK` to create a `MONTH_CUSTOMER` identifier, and projects details about first and last orders, dealer chains, dealer IDs, and both summarized and list-based KPI metrics related to customer lifecycle events like binding, newsales, porting, product changes, and terminations.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_KURT_CHAIN_AFFILIATION]]
| Column Name |
|---|
| CUSTOMER_SK |
| PERIOD_MONTH_KEY |
| NO_DEALER_CHAINS |
| NO_DEALER_IDS |
| LAST_ORDER_DT_KEY |
| LAST_DEALER_CHAIN |
| LAST_DEALER_ID |
| LAST_TERMINAL_DEALER_CHAIN |
| LAST_TERMINAL_DEALER_ID |
| LAST_TERMINAL_SOURCE_ORDER_ID |
| FIRST_ORDER_DT_KEY |
| FIRST_DEALER_CHAIN |
| FIRST_DEALER_ID |
| FIRST_TERMINAL_DEALER_CHAIN |
| FIRST_TERMINAL_DEALER_ID |
| FIRST_TERMINAL_SOURCE_ORDER_ID |
| ORDER_DT_KEY_LIST |
| DEALER_CHAIN_LIST |
| DEALER_ID_LIST |
| KPI_BINDING_LIST |
| KPI_NEWSALE_LIST |
| KPI_NEWSALE_TERMINAL_LIST |
| KPI_PORTING_INBOUND_LIST |
| KPI_PRODUCT_CHANGE_LIST |
| KPI_TERMINATION_LIST |
| KPI_GROSS_SALE_LIST |
| KPI_BINDING |
| KPI_NEWSALE |
| KPI_NEWSALE_TERMINAL |
| KPI_PORTING_INBOUND |
| KPI_PRODUCT_CHANGE |
| KPI_TERMINATION |
| KPI_GROSS_SALE |

