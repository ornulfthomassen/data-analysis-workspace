# KIM_PRODUCT_TREATMENT_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates information about 'treatments' (likely marketing offers or campaigns) by joining with related product details and handset information. It links a main treatment dimension to up to six associated products and handset specifications, creating a comprehensive dimension for analytical purposes.

## Data Sources (Inputs)
- ← [[KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_SK |
| TREATMENT_PRODUCT_KEY |
| TREATMENT_NM |
| TREATMENT_DESC |
| TREATMENT_CD |
| START_DATE |
| OFFER_CATEGORY |
| KPI_TYPE |
| END_DATE |
| CURRENT_VERSION_FLG |
| CURRENT_STATUS |
| BRAND |
| ACTION_CATEGORY_TYPE |
| ACTION_CATEGORY |
| HANDSET_KEY |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
| PRODUCT_KEY_5 |
| PRODUCT_KEY_6 |
- ← [[PRODUCT_DIM_VA]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
- ← [[HANDSET_DIM_VA]]
| Column Name |
|---|
| HANDSET_KEY |
| MARKETING_NAME |
| MANUFACTURER |

