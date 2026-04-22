# KIM_OB_CUST_CONTACT_HISTORY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts recent (last 7 days up to tomorrow) outbound customer contact history records, enriching them with comprehensive details about the customer (owner, payer, user), subscription (ID, main number, product, binding dates), associated campaign and communication (cell package, campaign, communication, channel), treatment, and handset (TAC_ID). A key function is to act as a delta feed for a fact table (`KIM_CAMPAIGN_DETAIL_FACT`), by excluding records that have already been processed and loaded into that target fact table for the same period and criteria.

## Data Sources (Inputs)
- ← [[CICDM.CI_CUST_CONTACT_HISTORY]]
- ← [[CICDM.CI_CELL_PACKAGE]]
- ← [[CICDM.CI_PACKAGE_X_TREATMENT]]
- ← [[CICDM.CI_SUBS_CONTACT_HISTORY]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]

