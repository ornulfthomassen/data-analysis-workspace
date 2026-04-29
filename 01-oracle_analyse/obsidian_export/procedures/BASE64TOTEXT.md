# BASE64TOTEXT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Decodes a Base64 encoded string to a plain text string. It processes the input Base64 string character by character, looking up its 6-bit binary representation from the `CCM.BASE64` table. These 6-bit segments are concatenated and then grouped into 24-bit blocks. Each 24-bit block is further split into three 8-bit segments (bytes). Each 8-bit segment is then looked up in the `CCM.ASCII` table to find its corresponding ASCII character. These decoded characters are concatenated to form the final plain text string, which is returned.

## Data Sources (Inputs)
- ← [[CCM.BASE64]]
| Column Name |
|---|
| CHARACTER |
| BINARY |
- ← [[CCM.ASCII]]
| Column Name |
|---|
| SYMBOL |
| BIN |

