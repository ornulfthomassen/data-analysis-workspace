# KIM_CONT_DEL

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Deletes records from the KIM_CAMPAIGN_DETAIL_FACT table for a specified date range. It iterates through records identified by a date key, deleting them one by one based on their contact key, and performs batch commits.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DATE_KEY |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |

