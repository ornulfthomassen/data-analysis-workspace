# V_ANALYTICAL_MASTER_TABLE_OTHR

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_ANALYTICAL_MASTER_TABLE_OTHR, creates a comprehensive, denormalized analytical dataset focused on 'Other' subscription types (e.g., Mobile, Fixed-line, Internet, TV) by combining various historical dimensions and fact tables. It consolidates monthly period data, subscription details, customer information, handset history, and aggregated usage/revenue metrics. The view filters out specific test/internal customers and includes detailed subscription attributes, device information, and aggregated usage statistics (data, MMS, SMS, voice) and revenue figures over the past three months for each subscription-month period. It serves as a master table for detailed analytical reporting and insights into these specific subscription categories.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]

