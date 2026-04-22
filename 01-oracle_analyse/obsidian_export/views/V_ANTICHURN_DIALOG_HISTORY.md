# V_ANTICHURN_DIALOG_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the history of anti-churn customer contacts, including contact details, associated subscription information, cell package details, communication specifics, and response history. It specifically filters for campaigns related to 'MPP_ANTICHURN' and 'MPR_ANTICHURN' with a campaign level greater than 0.

## Data Sources (Inputs)
- ← [[CICDM.CI_CUST_CONTACT_HISTORY]]
- ← [[CICDM.CI_SUBS_CONTACT_HISTORY]]
- ← [[CICDM.CI_CUST_RESPONSE_HISTORY]]
- ← [[CICDM.CI_RESPONSE]]
- ← [[CICDM.CI_CELL_PACKAGE]]
- ← [[CICDM.CI_CHANNEL]]
- ← [[CRM_ANALYSE.ADM_CAMPAIGN_CONFIG]]

