# GCP_AGREEMENT_INSURANCE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly quantities (opening, closing, new customers) for specific agreement insurance products, combining data from product facts with agreement offer and product dimensions. It joins this aggregated product data with a monthly date dimension to provide a time-series view of these key performance indicators, applying various filters to include specific product categories and exclude certain test data.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
| YEAR |
| MONTH_NUMBER |
| RELATIVE_MONTH |
- ← [[GALAXY.AGREE_PROD_MONTH_FACT_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| AGREEMENT_OFFER_KEY |
| AGREEMENT_PRODUCT_KEY |
| MARKET_AREA_KEY |
| AGREE_PRODUCT_QTY_OB |
| AGREE_PRODUCT_QTY_CB |
| AGREE_PRODUCT_QTY_NC |
- ← [[GALAXY.AGREEMENT_OFFER_DIM]]
| Column Name |
|---|
| AGREEMENT_OFFER_KEY |
| AGREEMENT_OFFER_NAME |
- ← [[GALAXY.AGREEMENT_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
| SOURCE_PRODUCT_ID_1 |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_PRODUCT_NEED |

