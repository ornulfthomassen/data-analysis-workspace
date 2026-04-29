# MAKE_MB_INCLUDED

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This is an Oracle SQL function named MAKE_MB_INCLUDED. It takes a string representing a data size (e.g., '1024 KB', '1.5 MB', '2 GB') as input. The function parses the string, converts any comma decimal separators to periods, removes the unit suffix (KB, MB, GB), and then converts the numeric value into its equivalent in Megabytes (MB). If the unit is Kilobytes (KB), it divides by 1024; if Megabytes (MB), it keeps the value as is; if Gigabytes (GB), it multiplies by 1024. If no recognized unit is found, or an error occurs during conversion, it returns NULL.

