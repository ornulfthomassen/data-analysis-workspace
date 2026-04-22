# FORMAT_NPS_CATEGORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Defines an Oracle SQL function named `FORMAT_NPS_CATEGORY`. This function takes a single numeric input, representing a 'likelihood to recommend' score (typically from 0 to 10), and categorizes it into one of three Net Promoter Score (NPS) categories: 'Promoter' (scores 9-10), 'Passive' (scores 7-8), or 'Detractor' (scores 0-6). It returns an empty string for NULL input and 'ERROR' for any other numeric input outside the defined range.

