# TMP_HEH_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Provides a filtered view of 'COMOYO_SUB_GRANT_EVENTS' data, specifically focusing on 'RightUsed' events. It excludes entries where the SKUS column starts with 'CMO-STO-' and includes a truncated string representation of the SKUS column.

## Data Sources (Inputs)
- ← [[COMOYO_SUB_GRANT_EVENTS]]
| Column Name |
|---|
| LOAD_DATE |
| EVENT_ID |
| EVENT |
| EVENT_TIME |
| USER_ID |
| GRANTOR |
| GRANTOR_CONTEXT |
| SKUS |
| SUBSCRIPTION_ID |
| RIGHT_ID |
| RIGHT_CREATOR |
| CREATOR_TYPE |
| SEQ_ID |
| RUN_ID |

