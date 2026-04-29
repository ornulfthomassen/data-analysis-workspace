# CHURN_AGRMT_REWARD_MPP_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Combines subscription details with agreement reward information by joining the `CHURN_SUBSCRIPTION_V` view and the `CHURN_AGRMT_REWARD` table on `PERIOD_MONTH_KEY` and `SUBSCRIPTION_KEY`.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCRIPTION_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
- ← [[CLM_ADM.CHURN_AGRMT_REWARD]]
| Column Name |
|---|
| AGREEMENT_ID |
| NO_MEMBERS |
| SUM_REWARD_UNITS |
| REWARD_AGRMT_ACTIVATED_FLG |
| REWARD_AGRMT_DEACTIVATED_FLG |
| REWARD_AGRMT_QUALIFIED_FLG |
| REWARD_AGRMT_DEQUALIFIED_FLG |
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |

