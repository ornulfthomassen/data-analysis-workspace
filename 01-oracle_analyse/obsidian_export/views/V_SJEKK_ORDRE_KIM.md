# V_SJEKK_ORDRE_KIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and consolidates information for new mobile postpaid orders that are linked to specific marketing campaigns in the 'KIM' system. It joins various campaign dimensions (treatment, communication, order match, response, channel, campaign) with campaign detail facts, order line details, and product dimensions. The view filters for 'new sale' actions and KPIs, specific product characteristics (mobile telephony, subscription, voice, postpaid), a particular source system, and a 30-day window after campaign contact, specifically for orders that have not yet been ranked.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KURT_ID_OWNER |
| CONTACT_DTTM |
| TREATMENT_KEY |
| COMMUNICATION_KEY |
| ORDER_MATCH_KEY |
| RESPONSE_KEY |
| CHANNEL_KEY |
| CAMPAIGN_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_RANK |
| MEASURE_TYPE |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_NM |
| OFFER_CATEGORY |
| PRODUCT_KEY_1 |
| ACTION_CATEGORY |
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| COMMUNICATION_NM |
| COMMUNICATION_CD |
| COMMUNICATION_KEY |
| ACTION_CATEGORY |
| OFFER_CATEGORY |
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM]]
| Column Name |
|---|
| ORDER_MATCH_KEY |
| ORDER_MATCH_GROUP |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_NM |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_NM |
- ← [[CRM_ANALYSE.ORDER_LINE_DETAIL_FACT_V]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| ORDERING_DT_KEY |
| KPI_NEWSALE |
| ORDERLINE_PRODUCT_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| CAMPAIGN_CD |
| CAMPAIGN_NM |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PAYMENT |

