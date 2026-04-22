# V_SCORING_TABLE_CUST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named V_SCORING_TABLE_CUST, provides a comprehensive, month-specific 360-degree profile of individual customers and their households for CRM analytics and scoring. It aggregates a wide range of data points including demographics (age, gender, birth details), contact preferences (email, SMS opt-in), residency, customer status, and segmentations (MAP2, lifecycle). It details household composition, geographical location (postal code, municipality, region), and network coverage for both mobile and fixed-line services (ADSL, VDSL). The view also includes counts of various product subscriptions (Mobile PostPaid, PrePaid, Mobile Broadband, Fixed, DSL, Fiber) at customer (owner), user, and household levels. Furthermore, it incorporates detailed usage statistics (data volume, SMS, voice minutes, revenue) over three-month periods for different product categories, trend variables, and information about the main user's subscription and associated device details (model, brand, OS, features). The view is likely used for customer segmentation, targeted marketing, risk assessment, or churn prediction.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
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

