# TEST_ORDER_1_DAY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, denormalized view of mobile order line transactions, enriching core order data with product, binding, dealer, location, customer demographics, campaign, and service provider details. It calculates various sales KPIs, categorizes product changes (upsale/downsale), and filters for specific mobile market areas and order statuses, focusing on recent activity and excluding a particular dealer.

## Data Sources (Inputs)
- ← [[galaxy.order_line_detail_fact_mv]]
| Column Name |
|---|
| ORDER_LINE_ID |
| ORDER_KEY |
| ORDER_LINE_KEY |
| SOURCE_ORDER_ID |
| ORDER_STATUS_DT_KEY |
| ORDER_DT_KEY |
| ORDERING_DT_KEY |
| AGREED_DELIVERY_DT_KEY |
| ORDER_LINE_TYPE_KEY |
| kpi_newsale |
| kpi_termination |
| kpi_porting_inbound |
| kpi_gross_sale |
| KPI_PRODUCT_CHANGE |
| CAMPAIGN_DATE_KEY |
| campaign_treatment_key |
| campaign_channel_key |
| campaign_hit_type_key |
| campaign_communication_key |
| campaign_ref_source_system_id |
| SUBSCR_OWNER_LOC_KEY |
| RESOURCE_VALUE |
| owner_customer_key |
| ORDER_SUBSCR_KEY |
| SERVICE_PROVIDER_FROM_KEY |
| SERVICE_PROVIDER_TO_KEY |
| orderline_product_key |
| subscr_prim_product_key |
| binding_type_benefit_key |
| dealer_key |
| business_area_key |
| market_area_key |
| order_status_key |
| handset_key |
| FROM_ORDER_PRODUCT_KEY |
| ORDER_STATUS_REASON_KEY |
- ← [[galaxy.product_dim]]
| Column Name |
|---|
| product_key |
| drm_common_brand |
| TK_INCOME_SERVICE |
| drm_common_portfolio |
| drm_common_product_area |
| drm_common_payment |
| PRODUCT_NAME |
| PRODUCT_DESC |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_REPORTING |
| PRODUCT_FAMILY_NAME |
| MONTHLY_PRICE |
| TK_PRODUCT_RANK |
- ← [[galaxy.binding_type_benefit_dim]]
| Column Name |
|---|
| binding_type_benefit_key |
| binding_type_desc |
| binding_benefit_desc |
- ← [[galaxy.dealer_dim]]
| Column Name |
|---|
| dealer_key |
| dealer_name |
| drm_sales_channel_gen02_desc |
| drm_sales_channel_gen03_desc |
| drm_sales_channel_gen04_desc |
| drm_sales_channel_gen05_desc |
| drm_sales_channel_gen07_desc |
| dealer_chain_name |
| POSTCODE_ID_MAIN |
| source_dealer_id |
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
| Column Name |
|---|
| POSTNUMMER |
| POSTSTED |
| FYLKEKODE |
| FYLKE |
| KOMMUNEKODE |
| KOMMUNE |
| LATITUDE |
| LONGITUDE |
- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]
| Column Name |
|---|
| KOMMUNEKODE |
| LATITUDE |
| LONGITUDE |
| POSTSTED |
| FYLKEKODE |
| FYLKE |
| KOMMUNE |
- ← [[galaxy.business_area_dim_v]]
| Column Name |
|---|
| business_area_key |
| business_area_name |
- ← [[galaxy.order_line_type_dim]]
| Column Name |
|---|
| orderline_type_key |
| orderline_type_desc |
| orderline_type_group_desc |
| orderline_type_category_desc |
- ← [[galaxy.market_area_dim]]
| Column Name |
|---|
| market_area_key |
- ← [[galaxy.order_status_dim_mv]]
| Column Name |
|---|
| order_status_key |
| ORDER_STATUS_NAME |
| SOURCE_SYSTEM_STATUS_CODE |
- ← [[galaxy.handset_dim_v]]
| Column Name |
|---|
| handset_key |
| handset_type |
| marketing_name |
| MANUFACTURER |
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
| Column Name |
|---|
| FROM_ORDER_PRODUCT_KEY |
| DRM_COMMON_BRAND |
| DRM_COMMON_PAYMENT |
| PRODUCT_NAME |
| PRODUCT_DESC |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_MARKET_PRODUCT |
| MONTHLY_PRICE |
| TK_PRODUCT_RANK |
- ← [[CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| DATE_OF_BIRTH |
- ← [[CRM_ANALYSE.HOUSEHOLD_LAT_LONG_SHOP_V]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| ANTALL_I_HUSSTAND |
| ADRESSE |
| POSTNR |
| KOMMUNENR |
| LATITUDE |
| LONGITUDE |
- ← [[GALAXY.BINDING_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| PRODUCT_NAME |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| treatment_key |
| TREATMENT_NM |
| TREATMENT_CD |
| TREATMENT_PRODUCT_DESC |
| ACTION_CATEGORY |
| ACTION_CATEGORY_TYPE |
| OFFER_CATEGORY |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_NM |
- ← [[GALAXY.CAMPAIGN_HIT_TYPE_DIM]]
| Column Name |
|---|
| campaign_hit_type_key |
| campaign_hit_type_DESC |
| campaign_hit_type_GROUP |
- ← [[CRM_ANALYSE.BR_ANALYTIC_UNIVERSE_SUBSET]]
| Column Name |
|---|
| MONTH_KURT_KEY |
| X_ALDER |
| X_ALDERSGRUPPE |
| X_KJONN |
| X_LIVSFASE |
| X_ENSLIG_PAR |
| X_BARN |
| X_SMAABARN |
| X_SKOLEBARN |
| X_POSTREKLAMESEGM_PERIOD_DEF |
| X_POSTREKLAMESEGMENTER_LAST1 |
| X_POSTREKLAMESEGMENTER_LAST2 |
| X_POSTREKLAMESEGMENTER_LAST3 |
| X_BOLIG_BY_LAND |
| X_ANTALL_I_HUSSTAND |
| X_BOLIGTYPE_ENKEL |
| X_BOLIGTYPE_DETALJ |
| X_HYTTEEIER |
| X_HYTTE_FJELL_600M |
| X_HYTTE_KYST_1KM |
| X_HYTTE_INNLAND |
| X_HYTTE_FJELLFYLKE |
| X_HYTTE_KYSTFYLKE |
| X_HYTTE_INNLANDSFYLKE |
| X_BILSEGMENT_NYESTE_BIL |
- ← [[CRM_ANALYSE.NRPORT_SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER_ID |
| SERVICE_PROVIDER_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| RELATIVE_WEEK |

