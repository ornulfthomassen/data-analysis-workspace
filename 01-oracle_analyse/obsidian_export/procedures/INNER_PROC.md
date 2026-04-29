# INNER_PROC

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Dynamically creates a temporary table named 'tmppp' that summarizes specific product offer configuration values by joining product offer data with configuration details from a materialized view, performing aggregations like min, max, and sum.

## Data Sources (Inputs)
- ← [[PCAT.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| CONFIGURATION_ID |
| configuration_value |

## Target Tables (Outputs)
- → [[tmppp]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| min_configuration_value |
| max_configuration_value |
| ny_pris |

