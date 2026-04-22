# GCP_ADM_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, monthly aggregated profile of customer information. It consolidates various customer-related attributes such as demographics (age, gender, birth month, life stage), household details (composition, age distribution), address and location data (postal code, municipality, house type), service coverage information (mobile, ADSL, VDSL), subscription counts (by product type for both customer and user level), revenue, and key usage metrics (active days, product days). The primary purpose, as indicated in the comments, is to prepare this enriched customer data for loading into a data platform referred to as 'Mjøsa'. It also includes filters to exclude known test customers.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_SUBS_CNT]]
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_CUSTOMER_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_USAGE_TREND]]
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]
- ← [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]

