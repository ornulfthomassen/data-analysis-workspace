# F_KURT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This is a PL/SQL function named F_KURT that takes a VARCHAR2 input parameter (P_IN) and returns a NUMBER. It acts as a lookup or mapping function, translating specific input names (case-insensitive) into predefined numerical identifiers. If the input is NULL, it returns -2. If the input name is not found in its internal list, it returns -1.

