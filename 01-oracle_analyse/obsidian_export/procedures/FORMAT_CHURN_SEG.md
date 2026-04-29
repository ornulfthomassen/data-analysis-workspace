# FORMAT_CHURN_SEG

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Translates a numerical churn segment identifier (P_IN) into a descriptive string label (e.g., 'Høy 1', 'Medium 1', 'Lav 1'). It handles NULL input by returning 'Ukjent' and includes specific remappings for certain numerical values before returning a trimmed string, or 'ERROR' for unhandled input numbers.

