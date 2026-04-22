# V_BR_ANALYTIC_UNIVERSE_ALL

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Creates a historical analytic universe for customers, combining monthly dimension data (spanning the last 24 months up to the previous month relative to the current date) with customer and household attributes from a historical analytic universe table. It generates unique composite keys for customer-month combinations for analytical tracking, providing a time-series view of customer and household characteristics.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.BRING_ANALYTIC_UNIVERSE_HIST]]

