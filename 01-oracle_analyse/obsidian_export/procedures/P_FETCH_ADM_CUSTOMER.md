# P_FETCH_ADM_CUSTOMER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_FETCH_ADM_CUSTOMER` dynamically creates two permanent tables, both following the naming convention `ADM_CUSTOMER_YYYYMM`, to store customer and household attribute data. One table is created for the previous month's data, sourced from `CCM.VYA_ADM_CUSTOMER`. The other table is created for the current month's data, sourced from `CCM.VYA_ADM_CUSTOMER_CURRENT`. Before creation, the procedure checks if these tables already exist and drops them if found. The creation of the current month's table is conditionally executed, only occurring if the current day of the month is between the 7th and 11th.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[CCM.VYA_ADM_CUSTOMER]]
- ← [[CCM.VYA_ADM_CUSTOMER_CURRENT]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_YYYYMM]]

