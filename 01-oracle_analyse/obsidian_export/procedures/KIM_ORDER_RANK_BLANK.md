# KIM_ORDER_RANK_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Sets the ORDER_RANK column to NULL for specific records in KIM_CAMPAIGN_DETAIL_FACT. It identifies records based on a date range, a fixed measure type (1), and two distinct source system keys (58 and 63), specifically targeting those where ORDER_RANK is not already NULL. The process is batched with periodic commits.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_DT_KEY |
| MEASURE_TYPE |
| SOURCE_SYSTEM_KEY |
| ORDER_RANK |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |

