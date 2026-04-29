# CUSTOMER_NUM_OF_EVENTS

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates the number of events (COUNT(1)) for specific event types, grouped by event node and main number. It then updates a 'NUM_OF_EVENTS' column in the 'CRM_ANALYSE.CUSTOMER_EVENTS' table with these calculated counts for the corresponding event records. The procedure processes data in batches, committing changes periodically.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| EVENT_NODE |
| MAIN_NUMBER |
| EVENT |
| KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| NUM_OF_EVENTS |

