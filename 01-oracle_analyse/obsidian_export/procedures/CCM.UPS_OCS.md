# UPS_OCS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Iterates through records in 'ccm.CCM_OC_PERSONALIZEDCAMPAIGN' where an offer has been accepted. For each record, it updates corresponding rows in 'CLM_CCM.CCM_OC_PERSONALIZEDCAMPAIGN' by populating the 'OFFERACCEPTED', 'OFFER_STATUS', and 'OFFER_STATUS_DATE' columns, but only if these target columns are currently NULL. The update is based on matching 'URLCODE'.

## Data Sources (Inputs)
- ← [[CCM.CCM_OC_PERSONALIZEDCAMPAIGN]]
| Column Name |
|---|
| URLCODE |
| OFFERACCEPTED |
| OFFER_STATUS |
| OFFER_STATUS_DATE |


## Target Tables (Outputs)
- → [[CLM_CCM.CCM_OC_PERSONALIZEDCAMPAIGN]]
| Column Name |
|---|
| OFFERACCEPTED |
| OFFER_STATUS |
| OFFER_STATUS_DATE |


