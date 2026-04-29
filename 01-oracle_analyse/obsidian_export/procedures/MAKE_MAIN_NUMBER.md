# MAKE_MAIN_NUMBER

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Converts a VARCHAR2 string into a NUMBER, employing robust error handling. It first attempts a direct numeric conversion of the trimmed input string. If this fails, it performs a series of string cleaning operations (replacing commas with periods, removing asterisks, hash signs, '+47' prefix, and spaces) before attempting conversion again using a specific numeric format mask ('999999.9999'). If both conversion attempts fail, the function returns NULL.

