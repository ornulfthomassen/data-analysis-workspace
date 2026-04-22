# V_RETENTION_DIALOG_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive historical record of customer interactions and dialogs specifically focused on retention campaigns. It consolidates details from customer contact history, subscription information, communication packages, campaign configurations (filtered by specific retention areas), communication channels, and customer responses to present a unified view of retention-related customer engagement.

## Data Sources (Inputs)
- ← [[CICDM.CI_CUST_CONTACT_HISTORY]]
- ← [[CICDM.CI_SUBS_CONTACT_HISTORY]]
- ← [[CICDM.CI_CUST_RESPONSE_HISTORY]]
- ← [[CICDM.CI_RESPONSE]]
- ← [[CICDM.CI_CELL_PACKAGE]]
- ← [[CICDM.CI_CHANNEL]]
- ← [[CRM_ANALYSE.ADM_CAMPAIGN_CONFIG]]

