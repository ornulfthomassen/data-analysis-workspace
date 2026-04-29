# KIM_CONTACT_SWAP_MATCH_KURT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure identifies and updates 'swap order match' details within the 'CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT' table. It aggregates and ranks specific order information from various GALAXY data mart tables (order lines, products, dates, dealers, order line types) and campaign detail facts. The procedure applies complex filtering and grouping to determine 'swap' related attributes like product key, timestamp, dealer key, order ID, and rank. It also logs the execution status and record counts into 'CLM_CCM.GOV_DQ_MARTS' and 'STLOG.ST_IN' tables.

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
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_DT_KEY |
| ORDER_TIME_KEY |
| OWNER_CUSTOMER_KEY |
| MARKET_AREA_KEY |
| NUMBER_OF_ORDERS |
| ORDERLINE_PRODUCT_KEY |
| ORDER_SUBSCR_KEY |
| ORDER_STATUS_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_STATUS_REASON_KEY |
| KPI_NEWSALE |
| DEALER_KEY |
| SOURCE_ORDER_ID |
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
| ORDERLINE_TYPE_KEY |
| ORDERLINE_TYPE_category_DESC |

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
| CONTACT_KEY |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |
| CHECK_SUM_TARGET |
| RUN_ID |
| SEQ_ID |

