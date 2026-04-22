# V_SJEKK_ORDRE_KIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view analyzes new sales orders for postpaid mobile telephony subscriptions that originated from CRM campaign contacts. It joins campaign details (contact date, communication, campaign, treatment, response, channel) with order details and product information. The view specifically filters for new sales (KPI_NEWSALE = 1) of postpaid mobile phone subscriptions, linking them to campaign contacts where the order date falls within 30 days of the contact date. It also applies filters based on measure type, source system, and communication/offer categories ('Nysalg' - New Sale, 'Mobilt Postpaid' - Mobile Postpaid), and only includes records where ORDER_RANK is null.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[CRM_ANALYSE.ORDER_LINE_DETAIL_FACT_V]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]

