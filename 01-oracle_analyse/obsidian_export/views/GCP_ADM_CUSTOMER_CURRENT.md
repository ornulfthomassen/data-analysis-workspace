# GCP_ADM_CUSTOMER_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'GCP_ADM_CUSTOMER_CURRENT', provides a comprehensive and current snapshot of customer and household data, enriched with demographic details, contact information, service coverage, subscription counts, revenue figures, and 3-month average usage. Its primary purpose is to prepare and load customer data into the 'Mjøsa' system (likely a data warehouse or analytical platform). It filters for specific customer types and statuses while excluding known test customer IDs, ensuring a clean and relevant dataset for analytical and reporting purposes.

## Data Sources (Inputs)
- ← [[ODS.CUSTOMER_ODS]]
- ← [[CCM.VYA_ADM_CURRENT_USAGE_MONTH]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CCDW.CUSTOMER]]
- ← [[ODS.CUSTOMER_RES_AND_APP]]
- ← [[CLM_CCM.CCM_CUST_CONTACT_ADDRESS_V]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO_V]]
- ← [[CLM_CCM.CCM_FAR_V]]
- ← [[CLM_CCM.CCM_COVERAGE_NEW_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]

