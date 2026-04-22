# T_ORDERLINE_NEWSALE

**Schema:** `CCM` | **Type:** `View`

## Description
Filters and ranks new order line sales records for specific consumer subscription products ('Abonnement', 'Tale', 'Frihet') from 2016 onwards, excluding certain dealers. It extracts details such as dealer name and sales channel descriptions, and assigns a dense rank to order lines for each unique 'resource_value' based on their order date (descending), allowing for easy identification of the latest new sales event for a given resource.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.DEALER_DIM]]

