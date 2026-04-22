# VYA_ODS_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
The `VYA_ODS_CUSTOMER` view consolidates and enriches comprehensive customer information from various operational data store (ODS), customer relationship management (CRM), and data warehouse (DW) sources. It provides a unified 360-degree view of customers, including core demographics (type, status, gender, age, birth year), key identifiers (customer_sk, household_sk), commercial details (name, organization number, average monthly amounts), aggregated Talkmore product usage counts, subscription numbers (mobile, fixed, FTV) for owners, payers, and users, traffic/fee details, and marketing consent/reservation statuses (for direct marketing, telemarketing, email, and SMS). It is designed to be a central customer dimension for downstream reporting or data loading processes, indicated by the comment 'Loading CUSTOMER-data to Mjøsa'. The view also includes a default placeholder record for unknown customers.

## Data Sources (Inputs)
- ← [[TALKMORE.TALKMORE_MATCH]]
- ← [[ODS.CUSTOMER_ODS]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[ODS.CUSTOMER_RES_AND_APP]]
- ← [[CCDW.CUSTOMER]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[DUAL]]

