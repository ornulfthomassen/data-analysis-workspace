# P_TRA_CHURN_FORECAST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_TRA_CHURN_FORECAST` is designed to calculate churn forecast metrics. It first determines key date and period boundaries (like the last period for forecasting and the last midnight timestamp) from historical churn data. It then creates an intermediate table (`TMP_CP_CHURN_CALC`) to derive various churn-related ratios (monthly, weekday, and weekend shares) based on these calculated dates. Finally, it uses these ratios to generate forecasted churn KPI values (e.g., `KPI_CHURN_FC`, `KPI_PORTING_OUTBOUND_FC`) by applying them to the historical churn data, storing the results in another table (`TMP_CHURN_FORECAST`). The procedure actively drops and recreates these tables for each execution.

## Data Sources (Inputs)
- ← [[ALL_OBJECTS]]
- ← [[DUAL]]
- ← [[CLM_ADM.CHURN_CHURN_V]]

## Target Tables (Outputs)
- → [[TMP_CP_CHURN_CALC]]
- → [[TMP_CHURN_FORECAST]]

