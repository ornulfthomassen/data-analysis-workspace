# VYA_AGREEMENT_INSURANCE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "VYA_AGREEMENT_INSURANCE_AGG", provides an aggregated monthly overview of agreement insurance products. It combines detailed date dimensions with aggregated quantities (opening balance, closing balance, new customers) for agreement products. The aggregation specifically targets two types of insurance: device insurance ('DEVICE' product group) and security/safety related products ('Sikkerhet' need). It serves to track KPIs and provide reporting on these specific insurance product categories.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DAY |
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
| DRM_COMMON_MARKET_PRODUCT |
| SOURCE_PRODUCT_ID_1 |
| DRM_PRODUCT_NEED |

