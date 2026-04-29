# CUSTOMER_EVENT_LAST_INVOICE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates the gross amount and event date of the most recent prior invoice event for specific customer events (those with a NULL `GROSS_AMOUNT_LAST_MONTH`), and then updates these calculated values into the `GROSS_AMOUNT_LAST_MONTH` and `EVENT_START_DATE` columns of the `CRM_ANALYSE.CUSTOMER_EVENTS` table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| KEY |
| MAIN_NUMBER |
| EVENT_DATE |
| GROSS_AMOUNT_LAST_MONTH |
| GROSS_AMOUNT |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.CUSTOMER_EVENTS]]
| Column Name |
|---|
| GROSS_AMOUNT_LAST_MONTH |
| EVENT_START_DATE |

