# P_ADM_SUBSCRIPTION_CORE_FIXBB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure extracts, transforms, and loads fixed broadband (FIXBB) subscription data. It processes raw subscription details from external sources, applies complex analytic functions to derive relationships and ranks between subscriptions, and consolidates the results into a core subscription table. The process involves creating temporary intermediate tables for staged processing, performing data cleansing (e.g., handling duplicate main numbers), and incrementally updating the final core table with new and changed records. It also manages backups of the primary target tables and index creation/statistics gathering for performance.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DEALER_DIM]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_SUBSCRIPTION_RAW_FIXBB]]
- → [[CLM_ADM.ADM_SUBSCRIPTION_RAW_FIXBB_BK]]
- → [[CLM_ADM.TMP_SUBSCRIPTION_CORE_FIXBB]]
- → [[CLM_ADM.TMP_SUBSCRIPTION_CORE_FIXBB_BK]]
- → [[CLM_ADM.ADM_SUBSCRIPTION_CORE_FIXBB]]
- → [[CLM_ADM.ADM_SUBSCRIPTION_CORE_FIXBB_BK]]

