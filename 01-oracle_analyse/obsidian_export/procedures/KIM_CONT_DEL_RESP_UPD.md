# KIM_CONT_DEL_RESP_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Processes campaign detail records and related customer responses for a given date range. It identifies `CONTACT_KEY`s within the specified `P_START_DATE` and `P_END_DATE` from `KIM_CAMPAIGN_DETAIL_FACT`. For each identified `CONTACT_KEY`, it deletes the corresponding record from `KIM_CAMPAIGN_DETAIL_FACT` and updates the `USED_FLG` to 0 and `CONTACT_KEY` to -1 in `KIM_CUSTOMER_RESPONSE`.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DATE_KEY |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
- → [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| USED_FLG |
| CONTACT_KEY |

