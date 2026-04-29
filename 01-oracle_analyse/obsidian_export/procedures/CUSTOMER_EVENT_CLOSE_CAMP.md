# CUSTOMER_EVENT_CLOSE_CAMP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates and updates `CLOSE_CAMP_DAYS` for customer events. It first determines the duration (in days) from a specified event (`P_EVENT`) to the earliest subsequent SMS campaign event for the same customer, storing this duration in the `CLOSE_CAMP_DAYS` field of the initial event. Subsequently, it marks remaining unclosed SMS campaign events (which are linked to an event of type `P_EVENT`) with a value of -1 in their `CLOSE_CAMP_DAYS` field.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| KEY |
| EVENT_DATE |
| MAIN_NUMBER |
| EVENT |
| CLOSE_CAMP_DAYS |
| EVENT_CHANNEL |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| CLOSE_CAMP_DAYS |
| KEY |

