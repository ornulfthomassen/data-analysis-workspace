# QA_STOCK

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Performs data quality (QA) checks on subscription stock counts from multiple source systems (GALAXY, CM, CCDW, ODS) for Prepaid and Postpaid payment types. It calculates deviations between different source systems, and records current counts and historical data quality status (OK/DEVIATION) for each source system and payment type into a governance data quality mart table.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| PRIM_PRODUCT_KEY |
| SUB_PRODUCT_KEY |
| SUBSCR_TYPE_STATUS_KEY |
- ← [[CLM_CCM.CCM_PRODUCT_DIM_GALAXY_ADJ]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PAYMENT |
| POID |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| INC_VALID_TO_DATE |
| SUBSCR_ID |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| CURRENT_STATUS |
| MARKET_AREA_ID |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
| CUSTOMER_ROLE_ID |
- ← [[GOV_DQ_MARTS]]
| Column Name |
|---|
| process_nm |
| end_time |
| last_ressult |
| runtime |
| status_nm |
- ← [[DK_1964_GALAXY]]
| Column Name |
|---|
| run_id |
| paytype |
| antall |
- ← [[DK_1964_SOI]]
| Column Name |
|---|
| run_id |
| paytype |
| antall |
- ← [[DK_1964_CCDW]]
| Column Name |
|---|
| run_id |
| paytype |
| antall |
- ← [[DK_1964_ODS]]
| Column Name |
|---|
| run_id |
| paytype |
| antall |

## Target Tables (Outputs)
- → [[DK_1964_GALAXY]]
| Column Name |
|---|
| RUN_ID |
| KODE |
| PAYTYPE |
| ANTALL |
- → [[DK_1964_SOI]]
| Column Name |
|---|
| RUN_ID |
| KODE |
| PAYTYPE |
| ANTALL |
- → [[DK_1964_CCDW]]
| Column Name |
|---|
| RUN_ID |
| KODE |
| PAYTYPE |
| ANTALL |
- → [[DK_1964_ODS]]
| Column Name |
|---|
| RUN_ID |
| KODE |
| PAYTYPE |
| ANTALL |
- → [[GOV_DQ_MARTS]]
| Column Name |
|---|
| runtime |
| FREQ |
| system_nm |
| process_nm |
| status_nm |
| reason |
| priority |
| start_time |
| end_time |
| prev_ok_dttm |
| prev_ok_ressult |
| diff |
| last_resullt |

