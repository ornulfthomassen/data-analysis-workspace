# V_CLM_LIVSFASE_SEGMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and assigns a 'CLM_LIVSFASE_SEGMENT' (Customer Lifecycle Segment) for each individual customer ('KURT_ID'). It enriches individual customer data (like AGE) with aggregated household information (e.g., number of household members, number of children, number of youth) derived from the same customer base. The segment is determined by a custom function 'FORMAT_CLM_LIVSFASE_SEGMENT' which takes age and household composition as input. It also provides a `PERIOD_MONTH_KEY` representing the previous month.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]

