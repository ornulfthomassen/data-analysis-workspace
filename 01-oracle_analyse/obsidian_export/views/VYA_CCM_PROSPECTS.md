# VYA_CCM_PROSPECTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_CCM_PROSPECTS, is designed for loading prospect data into Viya for forecasting. It identifies potential customer leads from 'CLM_CCM.ODS_LEADS_CONSUMER' that have a valid customer mapping in 'CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V'. Crucially, it filters out leads whose associated phone numbers have recently been involved in a 'port-in' order (within the last 60 days) for specific mobile carriers (Telenor, Talkmore, Dipper). The view outputs a customer key, categorizes the prospect type as 'MOBILE', provides KPI flags for mobile prospects, and includes a count of non-contactable phone numbers.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
- ← [[CLM_CCM.ODS_LEADS_CONSUMER]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

