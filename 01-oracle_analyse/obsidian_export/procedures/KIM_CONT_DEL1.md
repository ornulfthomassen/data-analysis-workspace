# KIM_CONT_DEL1

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in KIM_CAMPAIGN_DETAIL_FACT_EXT where PROGRAM is 'P98 ESP TRIGGER' and deletes them in batches. This effectively purges specific campaign detail fact records from the table.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| PROGRAM |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |

