# P_EXT_CHURN_AGRMT_REWARD

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Processes family bonus agreement details, filtering for active subscriptions with rewards. It identifies unique and duplicate records, aggregates reward unit information, and then computes temporal flags indicating agreement activation, deactivation, qualification, and dequalification states, storing all intermediate and final results in temporary tables.

## Data Sources (Inputs)
- ← [[CHURN_ADM_AGRMT_FAMILIEBONUS_DET_V]]
- ← [[TMP_CHURN_ADM_AGRMT_FAMILIEBONUS_DET]]
| Column Name |
|---|
| unit_sk |
| agreement_id |
| period_month |
| product_key |
| unit_customer_role |
| unit_type |
| reward |
- ← [[TMP_CHURN_CP_FB_DETAIL]]
| Column Name |
|---|
| subscription_key |
| AGREEMENT_ID |
| PERIOD_MONTH_KEY |
- ← [[CHURN_ADM_AGRMT_FAMILIEBONUS_AGG_V]]
| Column Name |
|---|
| AGREEMENT_ID |
| PERIOD_MONTH |
| no_members |
| sum_reward_units |
- ← [[TMP_CHURN_CP_FB_DETAIL_WITH_AGGR]]
| Column Name |
|---|
| subscription_key |
| agreement_id |
| PERIOD_MONTH_KEY |
| no_members |
| sum_reward_units |

## Target Tables (Outputs)
- → [[TMP_CHURN_ADM_AGRMT_FAMILIEBONUS_DET]]
- → [[TMP_CHURN_CP_FB_DETAIL]]
| Column Name |
|---|
| subscription_key |
| agreement_id |
| PERIOD_MONTH_KEY |
| product_key |
| unit_customer_role |
- → [[TMP_CHURN_CP_FB_DETAIL_DUP]]
| Column Name |
|---|
| subscription_key |
| agreement_id |
| PERIOD_MONTH_KEY |
| product_key |
| unit_customer_role |
- → [[TMP_CHURN_CP_FB_DETAIL_WITH_AGGR]]
| Column Name |
|---|
| subscription_key |
| AGREEMENT_ID |
| PERIOD_MONTH_KEY |
| no_members |
| sum_reward_units |
- → [[TMP_CHURN_AGRMT_REWARD]]
| Column Name |
|---|
| subscription_key |
| agreement_id |
| PERIOD_MONTH_KEY |
| no_members |
| sum_reward_units |
| reward_agrmt_activated_flg |
| reward_agrmt_deactivated_flg |
| reward_agrmt_qualified_flg |
| reward_agrmt_dequalified_flg |

