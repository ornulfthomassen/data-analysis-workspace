# P_ADM_SUBSCRIPTION_MASTER_HIS2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBSCRIPTION_MASTER_HIS2 orchestrates a complex ETL process to build a master historical subscription dataset. It performs several key operations across different subscription types (Fixed Broadband, Mobile, Fixed Telephony):

1.  **Raw Data Processing**: It creates `*_RAW2` tables (e.g., `ADM_FIX_BB_SUBSCRIPTION_RAW2`, `ADM_FIX_TLF_SUBSCRIPTION_RAW2`) by extracting and initially filtering subscription data from `CCDW.SUBSCRIPTION` and `GALAXY.PRODUCT_DIM` based on business area and product technology.
2.  **Core Data Aggregation and Transformation**: It processes the raw data into `*_CORE2` tables (e.g., `ADM_FIX_BB_SUBSCRIPTION_CORE2`, `ADM_MOB_SUBSCRIPTION_CORE2`, `ADM_FIX_TLF_SUBSCRIPTION_CORE2`). This involves detailed aggregations using window functions, joining with `GALAXY.DEALER_DIM` and `GALAXY.PRODUCT_DIM`, and calculating historical relationships between subscriptions (previous, original, past subscriptions) and the days between them. Intermediate `TMP_` tables are often created as staging areas for these core tables.
3.  **Porting Data Integration**: It extracts and processes number porting in and out events for mobile and fixed telephony (`TMP_MOB_SUBSCR_IN_PORT2`, `ADM_MOB_SUBSCR_IN_PORT2`, etc.) from `NRPORT.NRPORT_PORTERINGER`, linking them to `CCDW.SUBSCRIPTION` data.
4.  **Master Historical Table Creation**: Finally, it consolidates all the processed data (from mobile core subscriptions, subscription mappings, product configurations, and porting events) into a comprehensive `ADM_SUBSCRIPTION_MASTER_HIS2` table. This table provides a rich historical view of subscriptions, including details like market area changes, owner/payer/user history, product keys, and porting information.

Throughout the process, the procedure manages backup tables (`BDM_` prefixed tables), performs incremental inserts and updates, creates indexes, and gathers database statistics to maintain data quality and performance.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[ADM_FIX_BB_SUBSCRIPTION_RAW2]]
- ← [[TMP_FIX_BB_SUBSCRIPTION_CORE2]]
- ← [[ADM_FIX_BB_SUBSCRIPTION_CORE2]]
- ← [[ADM_MOB_SUBSCRIPTION_RAW2]]
- ← [[TMP_MOB_SUBSCRIPTION_CORE2]]
- ← [[ADM_MOB_SUBSCRIPTION_CORE2]]
- ← [[ADM_FIX_TLF_SUBSCRIPTION_RAW2]]
- ← [[TMP_FIX_TLF_SUBSCRIPTION_CORE2]]
- ← [[ADM_FIX_TLF_SUBSCRIPTION_CORE2]]
- ← [[TMP_MOB_SUBSCR_IN_PORT2]]
- ← [[ADM_MOB_SUBSCR_IN_PORT2]]
- ← [[TMP_MOB_SUBSCR_OUT_PORT2]]
- ← [[ADM_MOB_SUBSCR_OUT_PORT2]]
- ← [[TMP_FIX_TLF_SUBSCR_IN_PORT2]]
- ← [[ADM_FIX_TLF_SUBSCR_IN_PORT2]]
- ← [[TMP_FIX_TLF_SUBSCR_OUT_PORT2]]
- ← [[ADM_FIX_TLF_SUBSCR_OUT_PORT2]]

## Target Tables (Outputs)
- → [[ADM_FIX_BB_SUBSCRIPTION_RAW2]]
- → [[BDM_FIX_BB_SUBSCRIPTION_RAW2]]
- → [[TMP_FIX_BB_SUBSCRIPTION_CORE2]]
- → [[BDM_FIX_BB_SUBSCRIPTION_CORE2]]
- → [[ADM_FIX_BB_SUBSCRIPTION_CORE2]]
- → [[TMP_MOB_SUBSCRIPTION_CORE2]]
- → [[BDM_MOB_SUBSCRIPTION_CORE2]]
- → [[ADM_MOB_SUBSCRIPTION_CORE2]]
- → [[ADM_FIX_TLF_SUBSCRIPTION_RAW2]]
- → [[BDM_FIX_TLF_SUBSCRIPTION_RAW2]]
- → [[TMP_FIX_TLF_SUBSCRIPTION_CORE2]]
- → [[BDM_FIX_TLF_SUBSCRIPTION_CORE2]]
- → [[ADM_FIX_TLF_SUBSCRIPTION_CORE2]]
- → [[TMP_MOB_SUBSCR_IN_PORT2]]
- → [[BDM_MOB_SUBSCR_IN_PORT2]]
- → [[ADM_MOB_SUBSCR_IN_PORT2]]
- → [[TMP_MOB_SUBSCR_OUT_PORT2]]
- → [[BDM_MOB_SUBSCR_OUT_PORT2]]
- → [[ADM_MOB_SUBSCR_OUT_PORT2]]
- → [[TMP_FIX_TLF_SUBSCR_IN_PORT2]]
- → [[BDM_FIX_TLF_SUBSCR_IN_PORT2]]
- → [[ADM_FIX_TLF_SUBSCR_IN_PORT2]]
- → [[TMP_FIX_TLF_SUBSCR_OUT_PORT2]]
- → [[BDM_FIX_TLF_SUBSCR_OUT_PORT2]]
- → [[ADM_FIX_TLF_SUBSCR_OUT_PORT2]]
- → [[ADM_SUBSCRIPTION_MASTER_HIS2]]

