# P_CCM_TALKMORE_KURTMAPPING

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_CCM_TALKMORE_KURTMAPPING` is designed to map and enrich 'Talkmore' user and owner data with corresponding customer information from various data sources within a data warehouse environment. It performs a multi-stage, hierarchical matching process (identified by `MATCH_ID` 1 through 95) with progressively less strict criteria. 

1.  **Data Preparation**: It first aggregates Talkmore user and owner product usage data into a temporary customer table (`TMP_TALKMORE_CUSTOMER`) and extracts historical customer addresses into another temporary table (`TMP_CUSTOMER_HISTORIC_ADDRESS`).
2.  **Initial Population**: It initializes a main `TALKMORE_MATCH` table with the prepared Talkmore user data.
3.  **Cascading Matching**: It then iteratively updates the `TALKMORE_MATCH` table using 10 different matching algorithms. Each algorithm attempts to link unmatched Talkmore records (where `MATCH_ID IS NULL`) to customer records in the `GALAXY.CUSTOMER_DIM` table or other external sources, based on criteria such as:
    *   Exact matches on full name, birth date, and current address (`MATCH_ID=1`).
    *   Matches on full name, birth date, and historical address (`MATCH_ID=2`).
    *   Matches on first name, last name, birth date, and address (`MATCH_ID=3`).
    *   Partial name matches (e.g., first part of first name) combined with last name, birth date, and address (`MATCH_ID=4`, `MATCH_ID=5`).
    *   Matches on first name, birth date, and address (no last name match) (`MATCH_ID=6`).
    *   Matches on full name and address, but not birth date (`MATCH_ID=7`).
    *   Matches on full name, birth date, and postcode, but not street address (`MATCH_ID=8`).
    *   Matches against external consumer data (Evry/Dun & Bradstreet) via phone number (`MATCH_ID=90`).
    *   Address-only matches using `GALAXY.LOCATION_DIM` for records that couldn't be matched by customer demographics, creating dummy customer keys (`MATCH_ID=95`).
4.  **Enrichment**: For each successful match, the `TALKMORE_MATCH` table is updated with the matched `CUSTOMER_KEY`, `MASTER_ID`, customer names, address details, and other demographic information from the customer dimensions, along with the `MATCH_ID` and a description of the matching criterion. Records matched by a stricter criterion are excluded from subsequent, less strict matching attempts.

## Data Sources (Inputs)
- ← [[TALKMORE_USER]]
- ← [[TALKMORE_OWNER]]
- ← [[CRM_ANALYSE.TALKMORE_DETAILS_TMP]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
- ← [[CDC.MASTER_CUSTOMER]]
- ← [[CDC.ADDRESS_LINK]]
- ← [[CDC.ADDRESS]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[GALAXY.CUST_MAIN_LOC_DIM_V]]
- ← [[GALAXY.CUST_POST_LOC_DIM_V]]
- ← [[REFERENCE.CONSUMER_CUST_INFO]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[TALKMORE_MATCH]]
- ← [[TMP_TALKMORE_CUSTOMER]]
- ← [[TMP_CUSTOMER_HISTORIC_ADDRESS]]
- ← [[TMP_TALKMORE_MATCH1]]
- ← [[TMP_TALKMORE_MATCH2]]
- ← [[TMP_TALKMORE_MATCH3]]
- ← [[TMP_TALKMORE_MATCH4]]
- ← [[TMP_TALKMORE_MATCH5]]
- ← [[TMP_TALKMORE_MATCH6]]
- ← [[TMP_TALKMORE_MATCH7]]
- ← [[TMP_TALKMORE_MATCH8]]
- ← [[TMP_TALKMORE_MATCH90]]
- ← [[TMP_TALKMORE_MATCH95]]

## Target Tables (Outputs)
- → [[TALKMORE_MATCH]]
- → [[TMP_TALKMORE_CUSTOMER]]
- → [[TMP_CUSTOMER_HISTORIC_ADDRESS]]
- → [[TMP_TALKMORE_MATCH1]]
- → [[TMP_TALKMORE_MATCH2]]
- → [[TMP_TALKMORE_MATCH3]]
- → [[TMP_TALKMORE_MATCH4]]
- → [[TMP_TALKMORE_MATCH5]]
- → [[TMP_TALKMORE_MATCH6]]
- → [[TMP_TALKMORE_MATCH7]]
- → [[TMP_TALKMORE_MATCH8]]
- → [[TMP_TALKMORE_MATCH90]]
- → [[TMP_TALKMORE_MATCH95]]

