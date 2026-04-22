# V_ANALYTICAL_MASTER_TABLE_CUST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named `V_ANALYTICAL_MASTER_TABLE_CUST`, serves as a comprehensive, month-end analytical master table for customer and household information. It aggregates and denormalizes a wide range of data points including demographic details (age, gender, birthday), communication preferences (email, SMS opt-in), geographic location (postal code, municipality, county, region), household composition (number of members, age distribution within household), customer and subscription status, and customer segmentation (MAP2, livsfase). It extensively includes usage and revenue statistics for various product categories (Mobile PostPaid, Mobile PrePaid, Mobile Broadband, Fixed Line, DSL, Fiber) over recent months (last 1, 2, 3 months, and 3-month sums) for both customer owners and users, as well as longer-term usage trends. Additionally, it incorporates network coverage data (mobile, ADSL, VDSL) and main subscription device details (model, brand, OS, features). The view is designed to provide a 360-degree analytical profile of individual customers and their households, excluding specific test customers, for CRM, marketing analysis, and reporting purposes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_SUBS_CNT]]
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_CUSTOMER_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]
- ← [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]
- ← [[CLM_ADM.ADM_MAP2_SEGMENT_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_USAGE_TREND]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

