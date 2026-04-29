# V_RETENTION_DIALOG_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates customer contact, subscription, response, and campaign data, specifically filtering for retention-related campaigns. It provides a comprehensive history of customer interactions, including communication details, associated campaigns, and customer responses, with a focus on retention efforts for mobile, prepaid, and mobile broadband subscriptions.

## Data Sources (Inputs)
- ← [[CICDM.CI_CUST_CONTACT_HISTORY]]
| Column Name |
|---|
| KURT_ID |
| CONTACT_DTTM |
| CELL_PACKAGE_SK |
- ← [[CICDM.CI_SUBS_CONTACT_HISTORY]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| CELL_PACKAGE_SK |
| KURT_ID |
- ← [[CICDM.CI_CUST_RESPONSE_HISTORY]]
| Column Name |
|---|
| RESPONSE_DTTM |
| RESPONSE_CD |
| RESPONSE_CHANNEL_CD |
| CELL_PACKAGE_SK |
| KURT_ID |
- ← [[CICDM.CI_RESPONSE]]
| Column Name |
|---|
| RESPONSE_CD |
| RESPONSE_NM |
- ← [[CICDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| COMMUNICATION_SK |
| COMMUNICATION_OCCURRENCE_NO |
| COMMUNICATION_CD |
| CAMPAIGN_SK |
| CAMPAIGN_CD |
| CHANNEL_CD |
| COMMUNICATION_NM |
- ← [[CICDM.CI_CHANNEL]]
| Column Name |
|---|
| CHANNEL_CD |
| CHANNEL_NM |
- ← [[CRM_ANALYSE.ADM_CAMPAIGN_CONFIG]]
| Column Name |
|---|
| CAMPAIGN_CD |
| CAMPAIGN_AREA |
| CAMPAIGN_LEVEL |
| CAMPAIGN_DESC |
| CAMPAIGN_CHANNEL |

