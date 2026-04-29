# CUSTOMER_EVENT_NODE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in the CUSTOMER_EVENTS table, calculates an 'EVENT_NODE' value based on 'EVENT', 'EVENT_TYPE', and 'EVENT_CATEGORY' columns, and then updates the 'EVENT_NODE' column in the same CUSTOMER_EVENTS table for each record. It commits changes in batches of 1,000,000 records.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| KEY |
| EVENT |
| EVENT_TYPE |
| EVENT_CATEGORY |
| MAIN_NUMBER |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| EVENT_NODE |

