# VYA_FTV_QLIK_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a comprehensive sales data mart, primarily for Qlik reporting (indicated by 'QLIK_SALES' in the view name and source table). It aggregates sales orders, categorizes them based on various attributes like value chain, source system, product technology, and order type, and calculates recurring/non-recurring revenue. It enriches the core sales data with detailed date dimension attributes, campaign information, hardware details, and geographical data. The view includes extensive data transformation and categorization logic (e.g., `KPI_FLAG`, `ORDER_VALUECHAIN`, `SOURCE_SYSTEM` derivations) to provide a standardized and enriched dataset for sales analysis and reporting.

## Data Sources (Inputs)
- ← [[CLM_FIXED_CCM.QLIK_SALES_APP_ORDER]]
- ← [[GALAXY.DATE_DIM_MV]]

