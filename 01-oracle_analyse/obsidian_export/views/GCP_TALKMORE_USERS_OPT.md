# GCP_TALKMORE_USERS_OPT

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a standardized view of user option inventory data. It selects the ID, USER_ID, and OPT_TYPE_ID columns from the source table, casts them to VARCHAR2 with specified lengths, trims any leading/trailing spaces, and renames them to TALKMORE_USERS_OPT_ID, TALKMORE_USER_ID, and TALKMORE_TYPES_OPT_ID, respectively. This typically aims to ensure data type consistency and provide a clean interface for consuming user option-related identifiers.

## Data Sources (Inputs)
- ← [[TALKMORE.INVENTORY_USERS_OPT]]

