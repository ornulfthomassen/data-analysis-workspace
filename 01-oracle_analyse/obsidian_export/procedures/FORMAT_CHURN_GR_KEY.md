# FORMAT_CHURN_GR_KEY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL function calculates and returns a numerical churn group key based on three input parameters: a primary input value (P_IN), and two KPI indicators (P_KPI_PORT and P_KPI_TERM). It uses a CASE statement to evaluate specific ranges for P_IN combined with positive values for the KPI indicators to assign a corresponding churn group code. If no conditions are met, it returns -1, or NULL if P_IN is NULL.

