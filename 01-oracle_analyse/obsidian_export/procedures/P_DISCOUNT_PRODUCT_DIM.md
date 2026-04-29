# P_DISCOUNT_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure drops and recreates the 'DISCOUNT_PRODUCT_DIM' table. It populates this table by joining product offer configuration data with general product dimension information. The aim is to consolidate and calculate various types of price adjustments (overrides, NOK deductions, percentage deductions) related to product offers. Finally, it gathers statistics and creates indexes on the newly created table for performance optimization.

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
| CONFIGURATION_VALUE |
| CONFIGURATION_VALUE_DESCR |
| CONFIGURATION_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |

## Target Tables (Outputs)
- → [[DISCOUNT_PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| POID |
| CONFIGURATION_TYPE_ID |
| CONFIGURATION_TYPE |
| PRICE_OVERRIDE |
| PRICE_NOK_DEDUCTION |
| PRICE_PCT_DEDUCTION |

