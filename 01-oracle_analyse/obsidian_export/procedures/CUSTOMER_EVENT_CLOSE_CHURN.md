# CUSTOMER_EVENT_CLOSE_CHURN

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates the 'days to close churn' metric for customer events based on historical event patterns and updates the `CLOSE_CHURN_DAYS` column in the `CRM_ANALYSE.CUSTOMER_EVENTS` table with this metric.

## Data Sources (Inputs)
- ← [[CUSTOMER_EVENTS]]
| Column Name |
|---|
| KEY |
| EVENT_DATE |
| MAIN_NUMBER |
| EVENT_CATEGORY |
| EVENT |
| event_channel |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| CLOSE_CHURN_DAYS |

