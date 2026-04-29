# V_ANTICHURN_DIALOG_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and filters customer contact, subscription, and response history data, enriching it with cell package, channel, and campaign configuration details. Its primary purpose is to provide a comprehensive historical overview of customer dialogues specifically related to 'MPP_ANTICHURN' and 'MPR_ANTICHURN' campaigns, facilitating anti-churn analysis.

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
| RESPONSE_NM |
| RESPONSE_CD |
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
| CHANNEL_NM |
| CHANNEL_CD |
- ← [[CRM_ANALYSE.ADM_CAMPAIGN_CONFIG]]
| Column Name |
|---|
| CAMPAIGN_AREA |
| CAMPAIGN_LEVEL |
| CAMPAIGN_DESC |
| CAMPAIGN_CHANNEL |
| CAMPAIGN_CD |

