# F_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This is an Oracle SQL function named F_KURT. It takes a string (P_IN) as input, converts it to uppercase, and returns a predefined numeric identifier based on a hardcoded lookup of specific names. If the input is NULL, it returns -2. If the input name does not match any of the specified names, it returns -1. It essentially acts as a static mapping from certain names to specific numeric IDs.

