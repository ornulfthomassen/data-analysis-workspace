# F_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This PL/SQL function, F_KURT, takes a VARCHAR2 input (P_IN), likely a name, and translates it into a predefined numerical code or identifier. It performs a case-insensitive lookup. If the input is NULL, it returns -2. If the input matches one of the specified names (e.g., 'EVEN', 'HAAKON', 'ARILD', 'CHRISTINE'), it returns a corresponding number. If no match is found among the specified names, it returns -1. The script snippet contains syntax errors (e.g., misplaced `RETURN` and `V_RETURN` declaration, `TRIM` on a NUMBER), but the core logical intent of the `CASE` statement is for this lookup purpose.

