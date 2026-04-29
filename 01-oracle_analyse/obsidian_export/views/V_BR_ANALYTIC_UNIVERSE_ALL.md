# V_BR_ANALYTIC_UNIVERSE_ALL

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view constructs an 'analytic universe' by joining historical customer data from CLM_ADM.BRING_ANALYTIC_UNIVERSE_HIST with monthly time dimension data from CRM_ANALYSE.ADM_MONTH_DIM_V. It provides customer-related attributes like lifecycle stage and household composition for each relevant month, covering a recent 24-month historical period up to the previous month.

## Data Sources (Inputs)
- ← [[CLM_ADM.BRING_ANALYTIC_UNIVERSE_HIST]]
| Column Name |
|---|
| CUSTOMER_SK |
| X_SIST_OPPDATERT |
| X_LIVSFASE |
| X_BARN |
| X_SMAABARN |
| X_SKOLEBARN |
| X_SMAASKOLEBARN |
| X_TENAARINGSBARN |
| X_ANTALL_I_HUSSTAND |
| PERIOD_MONTH_KEY |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| LAST_DATE |
| RELATIVE_MONTH |

