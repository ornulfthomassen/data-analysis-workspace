# V_ANALYSE_CON_SUBSCR_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and de-duplicates customer subscription data from the `CON_SUBSCR_AGG` table. It specifically handles data anomalies for a particular month (201108) where multiple `RUN_ID`s might exist, merging these with standard data. It then applies a complex de-duplication logic using window functions (ranking by end date, original product start date, and user customer key) to select a single, most relevant record for each main subscription number.

## Data Sources (Inputs)
- ← [[CCDW_CONSUMERANALYSE.CON_SUBSCR_AGG]]
| Column Name |
|---|
| USER_CUSTOMER_KEY |
| MAIN_NUMBER |
| PERIOD_MONTH_KEY |
| PRIM_PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_BRAND |
| DRM_PRODUCT_BUSINESS_AREA_DET |
| DRM_MARKET_PRODUCT_GROUP |
| DRM_PRODUCT_ACCESS_PAYTYPE |
| MARKET_AREA_KEY |
| MARKET_AREA_DESC |
| PRIM_PROD_ORG_START_DT_KEY |
| PRIM_PROD_START_DT_KEY |
| PRIM_PROD_END_DT_KEY |
| BUSINESS_AREA_ID |
| BUSINESS_AREA_NAME |
| PRIM_PROD_BIND_END_DT_KEY |
| SUBSCR_NO_OF_SUB_PRODUCTS |
| USER_NO_OF_SUBSCR_FIXED |
| USER_NO_OF_SUBSCR_MOBILE |
| USER_NO_OF_SUBSCR_INTERNET |
| USER_NO_OF_SUBSCR_TOTAL |
| SERVICE_PROVIDER_ID_PORT_FROM |
| PORT_FROM_DATE |
| FRI_FAMILIE |
| RUN_ID |

