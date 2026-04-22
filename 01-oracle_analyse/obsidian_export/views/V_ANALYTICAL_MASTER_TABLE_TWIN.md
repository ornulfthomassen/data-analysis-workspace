# V_ANALYTICAL_MASTER_TABLE_TWIN

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a comprehensive monthly analytical master table by integrating historical subscription, customer, product, and device data. Its primary purpose is to link main subscriptions with associated 'twin' subscriptions/devices and specific 'data card' (Datakort1 and Datakort2) subscriptions, identified by unique product offer IDs. It generates various temporal keys (monthly and next-month) for subscriptions, main IDs, and customers, and filters the data to include specific customer types ('PU', 'P', 'PC') with active status ('K'), while excluding known test customer accounts, providing a consolidated dataset for in-depth historical analysis of subscription and device relationships.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCR_TWIN_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]

