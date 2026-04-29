# KIM_CONTACT_SWAP_MATCH_HOUSE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure identifies "swap order matches" for contact records based on household information. It queries various campaign, order, product, customer, date, dealer, and household-related tables to determine the earliest qualifying swap order for each contact, then updates the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT` table with the details of this matched swap order (product key, timestamp, dealer key, order ID, match type, and a calculated rank). It also logs the procedure's execution status, start/end times, and record counts into `CLM_CCM.GOV_DQ_MARTS` and `STLOG.ST_IN` tables for data quality and logging purposes.

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
| ORDER_TIME_KEY |
| DEALER_KEY |
| SOURCE_ORDER_ID |
| ORDERLINE_PRODUCT_KEY |
| OWNER_CUSTOMER_KEY |
| MARKET_AREA_KEY |
| NUMBER_OF_ORDERS |
| ORDER_SUBSCR_KEY |
| ORDER_STATUS_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_STATUS_REASON_KEY |
| KPI_NEWSALE |
| ORDER_LINE_TYPE_KEY |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
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
| CONTACT_KEY |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |
| CHECK_SUM_TARGET |
| RUN_ID |
| SEQ_ID |

