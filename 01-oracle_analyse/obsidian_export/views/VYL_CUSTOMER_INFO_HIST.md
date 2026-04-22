# VYL_CUSTOMER_INFO_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly snapshot of comprehensive customer and household profile information. It includes details such as customer and household surrogate keys, demographics (age, gender, month of birth), contact preferences (email/SMS indicators and acceptance flags), extensive residential information (postal codes, municipalities, housing types), customer type and status, household size, and a detailed breakdown of various product and service subscriptions (e.g., fixed telephony, TV, different internet types, mobile services, both from the primary provider and potentially others). The view filters the data to display information for a specific historical month, which is calculated based on the current system date (specifically, the YYYYMM of a date approximately one month and five days prior to SYSDATE). The primary purpose seems to be for historical reporting or analysis of customer data for a consistent past period.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]

