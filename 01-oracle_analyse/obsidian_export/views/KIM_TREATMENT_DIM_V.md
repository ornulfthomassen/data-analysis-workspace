# KIM_TREATMENT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, KIM_TREATMENT_DIM_V, serves as a consolidated dimension for treatment-related data. It combines core treatment attributes from KIM_TREATMENT_DIM with associated grouping information from KIM_TREATMENT_GROUP_DIM. The view applies data type casting and handles null values using NVL for several columns, preparing the data for analytical purposes.

## Data Sources (Inputs)
- ← [[KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_SK |
| TREATMENT_PRODUCT_KEY |
| TREATMENT_PRODUCT_DESC |
| TREATMENT_NM |
| TREATMENT_DESC |
| TREATMENT_CD |
| START_DATE |
| PRODUCT_KEY_6 |
| PRODUCT_KEY_5 |
| PRODUCT_KEY_4 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_1 |
| OFFER_CATEGORY |
| KPI_TYPE |
| HANDSET_KEY |
| END_DATE |
| CURRENT_VERSION_FLG |
| CURRENT_STATUS |
| BRAND |
| ACTION_CATEGORY_TYPE |
| ACTION_CATEGORY |
| CAMPAIGN_CATEGORY |
| CLM_PROGRAM |
| CLM_PLAN |
| CLM_CAMPAIGN |
| PRODUCT1 |
| PRODUCT2 |
| PRODUCT3 |
| PRODUCT4 |
- ← [[KIM_TREATMENT_GROUP_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_SUB_GROUP |
| TREATMENT_GROUP |
| TREATMENT_GROUP_SH |
| TREATMENT_CAMPAIGN |

