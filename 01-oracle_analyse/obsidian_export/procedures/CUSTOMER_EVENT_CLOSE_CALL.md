# CUSTOMER_EVENT_CLOSE_CALL

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure calculates and updates the 'CLOSE_CALL_DAYS' metric for records in the CRM_ANALYSE.CUSTOMER_EVENTS table. It operates in two main phases: 
1.  For customer events (E) matching the input parameter P_EVENT and specific channel/event criteria, it calculates the minimum positive time difference to a subsequent related event (C) for the same main number, then updates the E.CLOSE_CALL_DAYS for these main events with this duration.
2.  For other related customer events (C) that are linked to the P_EVENT events and still have a NULL CLOSE_CALL_DAYS, it sets their CLOSE_CALL_DAYS to -1. The procedure processes data in batches of 100,000 records, committing changes after each batch.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| KEY |
| EVENT_DATE |
| MAIN_NUMBER |
| EVENT |
| EVENT_CHANNEL |
| CLOSE_CALL_DAYS |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| CLOSE_CALL_DAYS |

