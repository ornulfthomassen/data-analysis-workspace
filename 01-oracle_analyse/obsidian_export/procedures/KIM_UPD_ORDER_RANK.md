# KIM_UPD_ORDER_RANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through specific campaign detail records within a given date range (start date only, end date parameter is unused) that have an existing order rank, and sets the 'ORDER_RANK' column to NULL for those records based on their contact key.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_RANK |
| ORDER_DT_KEY |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |
| CONTACT_KEY |

