# CHURN_AGRMT_REWARD_MPP_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view consolidates subscription details with agreement reward information. It joins subscription data with reward agreement data based on `PERIOD_MONTH_KEY` and `SUBSCRIPTION_KEY` to provide a unified perspective on subscription statuses, reward agreement activation/deactivation/qualification flags, the number of members, and the total reward units for each subscription per month. It likely serves to analyze the relationship between subscriptions and their associated reward programs, potentially for churn analysis or reward program effectiveness tracking.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCRIPTION_V]]
- ← [[CLM_ADM.CHURN_AGRMT_REWARD]]

