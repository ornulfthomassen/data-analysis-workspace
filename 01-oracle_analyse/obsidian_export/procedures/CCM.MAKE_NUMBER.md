# MAKE_NUMBER

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This is an Oracle PL/SQL function named MAKE_NUMBER. It aims to robustly convert a VARCHAR2 string input into a NUMBER. It first attempts a direct conversion after trimming whitespace. If that fails, it tries to convert the string by replacing commas with periods (to handle locale-specific decimal separators) and using a specific format mask. If both conversion attempts fail, the function returns NULL.

