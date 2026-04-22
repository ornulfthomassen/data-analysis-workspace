# V_CCM_OVERDUE_INVOICE_DATES

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to return key dates for the evaluation of overdue invoices. It calculates a start date (11 days prior to the most recent 'Type of Day 1' within the last 30 days, excluding today), a stop date (1 day prior to the most recent 'Type of Day 1' within the last 30 days, excluding today), the current date, and the type and day of the week for the current date. Special 'Type of Day' overrides are applied for specific holiday dates (May 17, Dec 24, Dec 31).

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]

