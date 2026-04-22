# VYA_TALKMORE_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named VYA_TALKMORE_CUSTOMER, is designed to provide a consolidated and standardized customer profile for 'Talkmore' customers. It extracts and transforms various customer attributes including demographics (age, gender, birth year/month), customer type and status, owner/user profiles, and counts of different Talkmore mobile and fixed-line products/subscriptions. It also includes placeholders for financial metrics and contact preferences, some of which are hardcoded. The primary purpose, as indicated in the comments, is to load this customer data into a data warehousing or analytical system referred to as 'Mjøsa'. It generates synthetic customer and household keys.

## Data Sources (Inputs)
- ← [[CLM_ADM.TALKMORE_MATCH]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]

