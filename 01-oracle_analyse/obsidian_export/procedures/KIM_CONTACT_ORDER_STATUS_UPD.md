# KIM_CONTACT_ORDER_STATUS_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates the order status in `KIM_CAMPAIGN_DETAIL_FACT` for specific campaign entries. It identifies orders where the current status in `KIM_CAMPAIGN_DETAIL_FACT` differs from the status in `GALAXY.ORDER_LINE_DETAIL_FACT_MV` under certain conditions (ranking and line item ID). The procedure also logs its execution status (start, completion) in the `CLM_CCM.GOV_DQ_MARTS` table.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_ID |
| ORDER_STATUS_KEY |
- ← [[KIM_ORDER_STATUS_RANK_V]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| RANK |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| SOURCE_ORDER_ID |
| ORDER_STATUS_KEY |
| ORDER_LINE_ID |
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_STATUS_KEY |

