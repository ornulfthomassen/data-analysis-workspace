# KIM_CAMP2773_V_OLD

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive and detailed dataset for analyzing a specific marketing campaign ('CAMP2773'). It enriches campaign contact and response data from the `kim_campaign_detail_fact` table with customer demographics, communication details, and related product order information (specifically orders with `PRODUCT_ACTION_TYPE_ID = 'PE'`) that occurred around the time of the contact. The view includes a wide array of attributes for understanding campaign performance, customer interactions, and the impact of contacts on product orders, focusing on data from 2017 onwards and valid main numbers.

## Data Sources (Inputs)
- ← [[crm_analyse.kim_campaign_detail_fact]]
- ← [[crm_analyse.kim_campaign_dim]]
- ← [[crm_analyse.kim_communication_dim]]
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER_PRODUCT]]

