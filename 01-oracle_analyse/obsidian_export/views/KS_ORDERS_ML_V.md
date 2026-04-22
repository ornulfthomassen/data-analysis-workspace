# KS_ORDERS_ML_V

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts and categorizes specific customer interaction and order data, primarily focusing on handled interactions related to mobile voice subscription products for consumers. It generates identifiers combining period and main numbers/Kurt IDs, and derives Key Performance Indicators (KPIs) like 'NEWSALE' or 'KPI_PRODUCT_CHANGE'. The view also includes records where the source order ID is null, suggesting an inclusion of initial or unlinked interactions, likely prepared for analytical or machine learning purposes.

## Data Sources (Inputs)
- ← [[KS_INTERACTION_ORDERMATCH]]

