# TEXTTOBASE64

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Converts an input VARCHAR string into its Base64 encoded representation. It achieves this by first looking up the binary representation of each input character from the 'CCM.ASCII' table, concatenating these binary strings. Then, it processes the combined binary string in 6-bit segments, looking up the corresponding Base64 character from the 'CCM.BASE64' table, and concatenating them to form the final Base64 output. It also handles padding for incomplete 24-bit blocks at the end of the input.

## Data Sources (Inputs)
- ← [[CCM.ASCII]]
| Column Name |
|---|
| BIN |
| SYMBOL |
- ← [[CCM.BASE64]]
| Column Name |
|---|
| CHARACTER |
| BINARY |

