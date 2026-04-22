# KIM_CANCEL_PORTING_V

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes porting-out orders (identified by PRODUCT_ACTION_TYPE_ID = 'PE') by linking them to customer campaign interactions. It captures details of orders, campaign activities, and communication events, specifically filtering for a particular campaign ('CAMP2773') and specific date ranges for orders and contacts. The view likely aims to understand the influence of marketing campaigns or communications on porting-out decisions or cancellations.

## Data Sources (Inputs)
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER_PRODUCT]]
- ← [[crm_analyse.kim_campaign_detail_fact]]
- ← [[crm_analyse.kim_campaign_dim]]
- ← [[crm_analyse.kim_communication_dim]]

