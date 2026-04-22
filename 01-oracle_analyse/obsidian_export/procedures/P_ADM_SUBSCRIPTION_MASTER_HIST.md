# P_ADM_SUBSCRIPTION_MASTER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure, `P_ADM_SUBSCRIPTION_MASTER_HIST`, is designed to construct and maintain a comprehensive historical view of customer subscriptions across various service types (mobile, fixed broadband, fixed telephony) by processing raw subscription data and integrating porting information. It involves multiple stages of data transformation:

1.  **Raw Data Preparation:** It creates initial 'raw' tables (e.g., `ADM_FIX_BB_SUBSCRIPTION_RAW`) by selecting and standardizing data from core `CCDW.SUBSCRIPTION` and `GALAXY.PRODUCT_DIM` tables, categorized by service type.
2.  **Core Data Derivation:** For each service type, it creates 'core' temporary/intermediate tables (e.g., `TMP_FIX_BB_SUBSCRIPTION_CORE`) by enriching the raw data with derived attributes such as `MAIN_NUMBER_RANK`, `FIRST_PARENT_SUBSCRIPTION_ID`, `LAST_OWNER`, `PREV_SUBSCRIPTION_ID`, `ORIG_SUBSCRIPTION_ID`, and `DAYS_BETWEEN_SUBSCRIPTIONS`, using analytical functions and joining with `GALAXY.DEALER_DIM`.
3.  **Core Table Maintenance:** It then loads and updates permanent 'core' tables (e.g., `ADM_FIX_BB_SUBSCRIPTION_CORE`) from these intermediate 'core' tables, inserting new records and updating existing ones.
4.  **Porting Data Integration:** It processes mobile and fixed telephony porting-in and porting-out events from `NRPORT.NRPORT_PORTERINGER`, joining with `CCDW.SUBSCRIPTION` and `CCDW.SUBSCRIPTION_MAPPING`, to create and maintain dedicated porting tables (e.g., `ADM_MOB_SUBSCR_IN_PORT`, `ADM_FIX_TLF_SUBSCR_OUT_PORT`).
5.  **Master History Creation:** Finally, it consolidates data from the `ADM_MOB_SUBSCRIPTION_CORE` table, `CCDW.SUBSCRIPTION_MAPPING`, `CRM_ANALYSE.PD`, and the mobile porting tables (`ADM_MOB_SUBSCR_IN_PORT`, `ADM_MOB_SUBSCR_OUT_PORT`) to build the ultimate `ADM_SUBSCRIPTION_MASTER_HIST` table, which serves as the final, enriched historical record.

The procedure also includes logic for creating backups (`BDM_...` and `B_TMP_...`) of tables before recreation/updates, gathering database statistics, and logging execution history via `CRM_ANALYSE.P_ADM_LOAD_HISTORY`. Several code blocks related to KAS (Cable Access System) TV and some KAS Broadband/Telephony specific processing are explicitly disabled with `AND 1=2` conditions in the provided script.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ADM_FIX_BB_SUBSCRIPTION_RAW]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[TMP_FIX_BB_SUBSCRIPTION_CORE]]
- ← [[ADM_FIX_BB_SUBSCRIPTION_CORE]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ADM_MOB_SUBSCR_IN_PORT]]
- ← [[TMP_MOB_SUBSCR_IN_PORT]]
- ← [[ADM_MOB_SUBSCR_OUT_PORT]]
- ← [[TMP_MOB_SUBSCR_OUT_PORT]]
- ← [[ADM_FIX_TLF_SUBSCR_IN_PORT]]
- ← [[TMP_FIX_TLF_SUBSCR_IN_PORT]]
- ← [[ADM_FIX_TLF_SUBSCR_OUT_PORT]]
- ← [[TMP_FIX_TLF_SUBSCR_OUT_PORT]]
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CRM_ANALYSE.PD]]
- ← [[ADM_PREV_ORIG_SUBS_MASTER]]
- ← [[ADM_PAST_ORIG_SUBS_MASTER]]
- ← [[ADM_FIX_TLF_SUBSCRIPTION_RAW]]
- ← [[TMP_FIX_TLF_SUBSCRIPTION_CORE]]
- ← [[ADM_FIX_TLF_SUBSCRIPTION_CORE]]
- ← [[ADM_MOB_SUBSCRIPTION_RAW]]
- ← [[TMP_MOB_SUBSCRIPTION_CORE]]

## Target Tables (Outputs)
- → [[ADM_FIX_BB_SUBSCRIPTION_RAW]]
- → [[BDM_FIX_BB_SUBSCRIPTION_RAW]]
- → [[TMP_FIX_BB_SUBSCRIPTION_CORE]]
- → [[B_TMP_FIX_BB_SUBSCRIPTION_CORE]]
- → [[ADM_FIX_BB_SUBSCRIPTION_CORE]]
- → [[BDM_FIX_BB_SUBSCRIPTION_CORE]]
- → [[ADM_MOB_SUBSCRIPTION_RAW]]
- → [[BDM_MOB_SUBSCRIPTION_RAW]]
- → [[TMP_MOB_SUBSCRIPTION_CORE]]
- → [[B_TMP_MOB_SUBSCRIPTION_CORE]]
- → [[ADM_MOB_SUBSCRIPTION_CORE]]
- → [[BDM_MOB_SUBSCRIPTION_CORE]]
- → [[ADM_KAS_BB_SUBSCRIPTION_RAW]]
- → [[BDM_KAS_BB_SUBSCRIPTION_RAW]]
- → [[TMP_KAS_BB_SUBSCRIPTION_CORE]]
- → [[B_TMP_KAS_BB_SUBSCRIPTION_CORE]]
- → [[ADM_KAS_BB_SUBSCRIPTION_CORE]]
- → [[BDM_KAS_BB_SUBSCRIPTION_CORE]]
- → [[ADM_KAS_TLF_SUBSCRIPTION_RAW]]
- → [[BDM_KAS_TLF_SUBSCRIPTION_RAW]]
- → [[TMP_KAS_TLF_SUBSCRIPTION_CORE]]
- → [[B_TMP_KAS_TLF_SUBSCRIPTION_CORE]]
- → [[ADM_KAS_TLF_SUBSCRIPTION_CORE]]
- → [[BDM_KAS_TLF_SUBSCRIPTION_CORE]]
- → [[TMP_MOB_SUBSCR_IN_PORT]]
- → [[ADM_MOB_SUBSCR_IN_PORT]]
- → [[BDM_MOB_SUBSCR_IN_PORT]]
- → [[TMP_MOB_SUBSCR_OUT_PORT]]
- → [[ADM_MOB_SUBSCR_OUT_PORT]]
- → [[BDM_MOB_SUBSCR_OUT_PORT]]
- → [[TMP_FIX_TLF_SUBSCR_IN_PORT]]
- → [[ADM_FIX_TLF_SUBSCR_IN_PORT]]
- → [[BDM_FIX_TLF_SUBSCR_IN_PORT]]
- → [[TMP_FIX_TLF_SUBSCR_OUT_PORT]]
- → [[ADM_FIX_TLF_SUBSCR_OUT_PORT]]
- → [[BDM_FIX_TLF_SUBSCR_OUT_PORT]]
- → [[ADM_SUBSCRIPTION_MASTER_HIST]]
- → [[ADM_FIX_TLF_SUBSCRIPTION_RAW]]
- → [[BDM_FIX_TLF_SUBSCRIPTION_RAW]]
- → [[TMP_FIX_TLF_SUBSCRIPTION_CORE]]
- → [[B_TMP_FIX_TLF_SUBSCRIPTION_CORE]]

