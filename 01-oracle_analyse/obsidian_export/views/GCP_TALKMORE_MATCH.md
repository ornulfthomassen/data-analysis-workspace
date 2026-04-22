# GCP_TALKMORE_MATCH

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `GCP_TALKMORE_MATCH`, provides a comprehensive set of customer and matching-related attributes. It appears to serve as a consolidated or flattened view of customer data, including personal details, company information, and various 'match' fields (e.g., `MATCH_FULL_NAME`, `MATCH_ADDRESS`, `MATCH_DATE_OF_BIRTH`). The view applies minor data cleaning/formatting such as trimming whitespace from IDs and padding ZIP codes with leading zeros if they are shorter than 4 characters. It also includes several flags related to different user/owner types (`NO_TKM_MPP_USER`, etc.) and general customer metadata (customer key, master ID, status, tags, household key, and main/postal address details). The overall purpose is likely to present a unified and slightly pre-processed dataset for customer matching or analysis within a 'Talkmore' system context.

## Data Sources (Inputs)
- ← [[TALKMORE.TALKMORE_MATCH]]

