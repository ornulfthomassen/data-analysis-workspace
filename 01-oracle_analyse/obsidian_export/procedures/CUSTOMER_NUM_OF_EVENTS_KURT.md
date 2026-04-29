# CUSTOMER_NUM_OF_EVENTS_KURT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure calculates the aggregated count of events (`NUM_OF_EVENTS`) for a given event type (`p_event`), filtering by `KEY IS NOT NULL` and `MAIN_NUMBER IS NULL`, and grouping by `EVENT_NODE` and `MAIN_NUMBER` from the `CUSTOMER_EVENTS` table. It then updates the `NUM_OF_EVENTS` column in the `CRM_ANALYSE.CUSTOMER_EVENTS` table with these calculated counts, matching records by `EVENT_NODE`, `KURT_ID_OWNER`, and `EVENT`.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| EVENT_NODE |
| KURT_ID_OWNER |
| EVENT |
| KEY |
| MAIN_NUMBER |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| NUM_OF_EVENTS |

