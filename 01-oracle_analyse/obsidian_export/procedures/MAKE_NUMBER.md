# MAKE_NUMBER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Converts a VARCHAR2 string to a NUMBER, robustly handling common formatting issues such as leading/trailing spaces and using a comma as a decimal separator. If conversion fails after two attempts, it returns NULL.

