# KIM_TREATMENT_CDM_TO_KIM_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through specific records in `KIM_CAMPAIGN_DETAIL_FACT` that meet certain criteria (ORDER_MATCH_KEY > 0 and BINDING_BENEFIT_DESC not in a predefined list). For each qualifying record, it calculates a new `BINDING_BENEFIT_DESC` value by joining with `GALAXY.ORDER_LINE_DETAIL_FACT_MV`, `GALAXY.ORDER_LINE_PRODUCT_DIM_V`, and `GALAXY.BINDING_TYPE_BENEFIT_DIM`, and then updates the `BINDING_BENEFIT_DESC` column in `KIM_CAMPAIGN_DETAIL_FACT` for that record. Commits are performed periodically and at the end.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_ID |
| ORDER_MATCH_KEY |
| BINDING_BENEFIT_DESC |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| SOURCE_ORDER_ID |
| ORDERLINE_PRODUCT_KEY |
| BINDING_TYPE_BENEFIT_KEY |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
| Column Name |
|---|
| BINDING_TYPE_BENEFIT_KEY |
| BINDING_BENEFIT_DESC |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| BINDING_BENEFIT_DESC |
| CONTACT_KEY |

