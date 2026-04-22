# P_CCM_TALKMORE_CUSTOMER_MAPPING

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_CCM_TALKMORE_CUSTOMER_MAPPING` implements a multi-stage customer matching and data enrichment process. It iteratively identifies and maps Talkmore customer records (initially stored in `TALKMORE_MATCH`) to detailed customer information from various source systems, primarily GALAXY, REFERENCE, and CDC schemas. It applies a series of increasingly relaxed matching rules based on combinations of names (full, first, last), date of birth, and current/historical addresses. For each matching rule, it creates a temporary table (`TMP_TALKMORE_MATCHX`) to store potential matches that haven't been resolved by previous, stricter rules. Finally, it updates the main `TALKMORE_MATCH` table with the matched customer demographic and address details, along with a `MATCH_ID` and `MATCH_DESC` indicating the successful matching criteria. The procedure also pre-processes historical address data into `TMP_CUSTOMER_HISTORIC_ADDRESS` and customer subscription details into `TMP_TALKMORE_CUSTOMER` for use in the matching steps.

## Data Sources (Inputs)
- ← [[TALKMORE_MATCH]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[GALAXY.CUST_MAIN_LOC_DIM_V]]
- ← [[GALAXY.CUST_POST_LOC_DIM_V]]
- ← [[TALKMORE.INVENTORY_USERS]]
- ← [[TALKMORE.INVENTORY_SUBSCR_MOBILE]]
- ← [[TALKMORE.INVENTORY_RATE_PLAN]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
- ← [[REFERENCE.CONSUMER_CUST_INFO]]
- ← [[CDC.MASTER_CUSTOMER]]
- ← [[CDC.ADDRESS_LINK]]
- ← [[CDC.ADDRESS]]

## Target Tables (Outputs)
- → [[TALKMORE_MATCH]]
- → [[TMP_TALKMORE_MATCH1]]
- → [[TMP_TALKMORE_MATCH2]]
- → [[TMP_TALKMORE_MATCH3]]
- → [[TMP_TALKMORE_MATCH4]]
- → [[TMP_TALKMORE_MATCH5]]
- → [[TMP_TALKMORE_MATCH6]]
- → [[TMP_TALKMORE_MATCH7]]
- → [[TMP_TALKMORE_MATCH8]]
- → [[TMP_TALKMORE_MATCH9]]
- → [[TMP_TALKMORE_MATCH10]]
- → [[TMP_TALKMORE_MATCH11]]
- → [[TMP_TALKMORE_MATCH12]]
- → [[TMP_TALKMORE_MATCH13]]
- → [[TMP_TALKMORE_MATCH14]]
- → [[TMP_TALKMORE_MATCH15]]
- → [[TMP_TALKMORE_MATCH16]]
- → [[TMP_TALKMORE_MATCH90]]
- → [[TMP_TALKMORE_MATCH95]]
- → [[TMP_TALKMORE_MATCH96]]
- → [[TMP_CUSTOMER_HISTORIC_ADDRESS]]
- → [[TMP_TALKMORE_CUSTOMER]]

