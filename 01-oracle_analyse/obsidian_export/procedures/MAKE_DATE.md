# MAKE_DATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Converts a string representation of a date or datetime into an Oracle DATE data type. It first attempts to parse the string using the 'YYYYMMDDHH24MI' format. If that fails, it tries parsing the first 8 characters of the string using the 'YYYYMMDD' format. If both attempts fail, the function returns NULL.

