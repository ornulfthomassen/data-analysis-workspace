# GCP_TALKMORE_USERS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a standardized and slightly cleaned dataset of Talkmore user information. It consolidates various personal and account details such as user IDs, account IDs, company information, names, addresses, contact numbers, email, birthdate, and account type. Data transformations include trimming whitespace from IDs, padding ZIP codes with leading zeros to ensure a minimum length of 4, and casting phone numbers and personal IDs to specific VARCHAR2 types. The purpose is to prepare this user data for consumption within the CCM schema, potentially for GCP-related processes or reporting.

## Data Sources (Inputs)
- ← [[TALKMORE.INVENTORY_USERS]]

