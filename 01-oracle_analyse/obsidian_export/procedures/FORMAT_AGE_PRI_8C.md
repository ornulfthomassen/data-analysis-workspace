# FORMAT_AGE_PRI_8C

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The script defines an Oracle SQL function named `FORMAT_AGE_PRI_8C`. This function takes a single numeric input, `P_IN` (presumably representing an age), and categorizes it into various age ranges or special conditions (e.g., NULL, -1, -2). It returns a `VARCHAR2` code corresponding to the determined category. The comments suggest that these codes are intended to represent specific age group descriptions (e.g., '18-28', 'Over 75'). The function handles edge cases and specific age bands, assigning a unique code for each. There are some overlaps/inconsistencies in the defined age ranges within the `CASE` statement itself, but the core purpose is age categorization.

