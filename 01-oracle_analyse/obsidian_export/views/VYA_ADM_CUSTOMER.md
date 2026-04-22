# VYA_ADM_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view, `VYA_ADM_CUSTOMER`, is designed to create a comprehensive, monthly aggregated customer profile for loading into a system called 'Mjøsa'. It focuses on private and active customers, excluding specific test accounts. The view consolidates various customer-related data points, including demographic information (age, gender, birth month), household details (number of members by age group), communication preferences (email/SMS opt-in), geographical data (postal code, municipality, area), network coverage details (mobile, ADSL, VDSL), product subscription counts (Mobile Postpaid, Prepaid, Mobile Broadband, Fixed, DSL, Fiber) for both customer owner and user roles, customer status, aggregated revenue, and subscription usage statistics (days active/productive, average 3-month revenue/data). It also includes details about the main user subscription type.

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

