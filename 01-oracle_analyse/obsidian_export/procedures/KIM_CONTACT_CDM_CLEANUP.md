# KIM_CONTACT_CDM_CLEANUP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Modifies the ORDER_RANK column in the KIM_CAMPAIGN_DETAIL_FACT table. It identifies specific ORDER_ID records based on CONTACT_DATE_KEY, MEASURE_TYPE, and SOURCE_SYSTEM_KEY. For these identified ORDER_ID's, it performs two types of updates: setting ORDER_RANK to NULL for records with MEASURE_TYPE = 1, and negating ORDER_RANK for records with MEASURE_TYPE = 5 and a positive rank.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_ID |
| CONTACT_DATE_KEY |
| MEASURE_TYPE |
| SOURCE_SYSTEM_KEY |
| ORDER_RANK |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |

