# V_MPORT_TAVLA_TREATED_STATUS

**Schema:** `CCM` | **Type:** `View`

## Description
This view summarizes the volume of distinct main numbers, providing an 'AC_BEHANDLING' (treatment status) based on campaign participation from `KIM_CAMPAIGN_DIM` and filtering out records associated with specific service providers ('Talkmore%' or 'Dipper%'). It groups results by order arrival date, service provider name, order status, and the calculated treatment status.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.V_MPORT_TAVLA]]
| Column Name |
|---|
| MAIN_NUMBER |
| ORDER_ARRIVAL_DATE |
| SERVICE_PROVIDER_ID_OUT_NAME |
| ORDER_STATUS_ID |
- ← [[CLM_CCM.CCM_DIALOG_HISTORY]]
| Column Name |
|---|
| MAIN_NUMBER |
| CONTACT_DTTM |
| CAMPAIGN_CD |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_CD |
| CAMPAIGN_GROUP_SK |

