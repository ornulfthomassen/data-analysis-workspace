# VYAMN_RESPONSES_STG_CI360

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYAMN_RESPONSES_STG_CI360`, serves as a staging or consolidated source for customer responses originating from a SAS Customer Intelligence 360 (CI360) system. It collects distinct response events, enriches them with detailed response attributes (like channel, reason, group, rank), and links them to customer and subscription master data. The view provides various temporal keys (date, month, week) and customer identifiers (customer owner, subscription, main number) to enable comprehensive analysis of customer interactions and campaign effectiveness.

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_RESPONSES]]
- ← [[SAS360_COMMON.SAS360_CI_RESPONSE]]
- ← [[SAS360_COMMON.SAS360_CCM_RESPONSE_REASON]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

