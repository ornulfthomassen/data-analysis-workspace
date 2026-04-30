# MAKE_DATE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Converts an input string into a timestamp. It first attempts to parse the string using 'YYYYMMDDHH24MISS' format. If that fails, it tries to parse the first 8 characters using 'YYYYMMDD' format. If both attempts fail, the function returns NULL.

