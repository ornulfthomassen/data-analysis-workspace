# KIM_RESPONSE_KEY_BOUNCE_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies campaign detail records associated with 'bounce' responses based on specific criteria (response name containing 'Bounce', certain response keys excluded, and a recent contact date). It then updates the 'RESPONSE_KEY' for these identified records in the KIM_CAMPAIGN_DETAIL_FACT table, mapping external response information ('Soft', 'Hard', 'Unknown'/'Informatio') to specific new response keys (59, 60, 61 respectively).

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_KEY |
| CUST_RESPONSE_KEY |
| CONTACT_DATE_KEY |
| EXTERNAL_RESPONSE_INFO_ID1 |
- ← [[KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_NM |
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| RESPONSE_CD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| RESPONSE_KEY |

