# P_RESPONSE_MATCH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates the `CONTACT_KEY` in the `KIM_CUSTOMER_RESPONSE` table. It identifies records in `KIM_CUSTOMER_RESPONSE` that need their `CONTACT_KEY` updated to a value derived from `KIM_CAMPAIGN_DETAIL_FACT` records, considering various join conditions with `KIM_TREATMENT_DIM` and filtering by `SOURCE_SYSTEM_KEY`. The process involves selecting relevant contact information, then iteratively updating `KIM_CUSTOMER_RESPONSE` rows. It also drops and recreates a specific index (`KCR_CONTACTED_KEY_IX`) on the `KIM_CUSTOMER_RESPONSE` table, likely for performance optimization during and after the update operation.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| TREATMENT_SK |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
| SOURCE_SYSTEM_KEY |
| RESPONSE_DTTM |
| CONTACT_KEY |
| CUST_RESPONSE_KEY |
- ← [[KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_SK |
| TREATMENT_KEY |
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DTTM |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
| SOURCE_SYSTEM_KEY |
| MEASURE_TYPE |
| TREATMENT_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |

