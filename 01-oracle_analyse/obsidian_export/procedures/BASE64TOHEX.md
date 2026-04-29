# BASE64TOHEX

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Converts an input Base64 encoded string into its hexadecimal representation. It performs this by looking up the 6-bit binary equivalent for each Base64 character from the 'ccm.base64' table, concatenating these binary strings, and then converting 8-bit segments of the resulting binary string into 2-character hexadecimal values using the 'ccm.ascii' table.

## Data Sources (Inputs)
- ← [[ccm.base64]]
| Column Name |
|---|
| binary |
| CHARACTER |
- ← [[ccm.ascii]]
| Column Name |
|---|
| BIN |
| HEX |

