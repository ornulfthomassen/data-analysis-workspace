# FORMAT_AGE_8C

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This function categorizes a given numeric input, typically representing an age, into predefined age range strings. It handles special values like NULL, -1, -2 by returning 'Unknown' or 'N/A', and returns specific age range strings for various numeric intervals. It also includes some overlapping or potentially redundant age range definitions (e.g., '67-74' and '65-74', '50-66' and '55-64'). If the input falls outside all defined ranges, it returns 'ERROR'.

