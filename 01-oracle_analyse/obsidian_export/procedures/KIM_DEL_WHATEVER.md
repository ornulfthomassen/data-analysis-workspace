# KIM_DEL_WHATEVER

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Deletes records from the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table. The `CONTACT_KEY` values for deletion are sourced from the `DUPL_SOURCE_CONT` table, specifically targeting `CONTACT_KEY`s that are identified as duplicates based on `SOURCE_CONTACT_ID` (i.e., not the first ranked occurrence). Additionally, deleted records from `KIM_CAMPAIGN_DETAIL_FACT` must have a `CONTACT_DATE_KEY` greater than '20170206'. The procedure commits changes in batches of 10 million records.

## Data Sources (Inputs)
- ← [[DUPL_SOURCE_CONT]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_CONTACT_ID |
| ORDER_RANK |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DATE_KEY |

