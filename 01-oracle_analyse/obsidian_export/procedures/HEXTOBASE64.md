# HEXTOBASE64

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This function, named HEXTOBASE64, attempts to convert a hexadecimal string to its Base64 equivalent. However, it contains several critical issues: the input parameter `V_HEX` is immediately shadowed and overwritten by a hardcoded hexadecimal value; only the first part of the conversion (looking up binary representations from `CCM.ASCII` based on hex characters) is active; and the main Base64 encoding logic, as well as the final `RETURN` statement, are commented out. As a result, the function will not return a value and will fail at runtime.

## Data Sources (Inputs)
- ← [[CCM.ASCII]]
| Column Name |
|---|
| BIN |
| HEX |

