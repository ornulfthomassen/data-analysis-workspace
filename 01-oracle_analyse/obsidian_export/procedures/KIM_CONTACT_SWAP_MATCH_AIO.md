# KIM_CONTACT_SWAP_MATCH_AIO

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure identifies and matches 'Swap Orders' to contact records in the `kim_campaign_detail_fact_EXT` table. It uses a multi-faceted approach, attempting to match orders first by 'Main Number', then by 'Kurt ID', and finally by 'Household ID'. For each contact record, it selects the best matching swap order based on specific criteria (e.g., product family name 'Telenor Swap nedbetalingsavtale', order status, and time windows), and then updates the contact's record with the details of the matched swap order, including product key, order timestamp, dealer key, order ID, and the type of match (MAIN_NUMBER, OWNER_KURT, or HOUSEHOLD). The procedure also logs its execution status and record counts to `CLM_CCM.GOV_DQ_MARTS` and `STLOG.ST_IN`.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
| PRODUCT_TP2 |
| DIALOG_ID |
| SWAP_RANK |
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DTTM |
| CONTACT_DATE_KEY |
| MAIN_NUMBER |
| KURT_ID_OWNER |
| CUST_HOUSEHOLD_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_DT_KEY |
| SOURCE_ORDER_ID |
| ORDER_TIME_KEY |
| DEALER_KEY |
| RESOURCE_VALUE |
| MARKET_AREA_KEY |
| NUMBER_OF_ORDERS |
| ORDERLINE_PRODUCT_KEY |
| ORDER_SUBSCR_KEY |
| ORDER_STATUS_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_STATUS_REASON_KEY |
| KPI_NEWSALE |
| OWNER_CUSTOMER_KEY |
| ORDER_LINE_TYPE_KEY |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| SOURCE_DEALER_ID |
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
| Column Name |
|---|
| ORDER_LINE_TYPE_KEY |
| ORDERLINE_TYPE_category_DESC |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
- ← [[CLM_KIM.CCM_HOUSEHOLD_INFO]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| START_DATE |
| END_DATE |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| SWAP_PRODUCT_KEY |
| SWAP_DTTM |
| SWAP_DEALER_KEY |
| SWAP_ORDER_ID |
| SWAP_MATCH |
| SWAP_RANK |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |
| CHECK_SUM_TARGET |

