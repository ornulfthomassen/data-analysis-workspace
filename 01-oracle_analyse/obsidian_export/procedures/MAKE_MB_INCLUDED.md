# MAKE_MB_INCLUDED

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL function, `MAKE_MB_INCLUDED`, is intended to parse a string that represents a data size (e.g., '1.5GB', '512KB', '10MB') and convert it into a numeric value expressed in Megabytes (MB). It identifies units 'GB', 'KB', and 'MB'. 'GB' values are multiplied by 1024 to convert to MB, 'KB' values are divided by 1024, and 'MB' values are taken directly. The function also handles European-style decimal separators (commas) by replacing them with periods before conversion. If the input string does not contain a recognizable unit, or if a conversion error occurs, the function is designed to return NULL.

