# GCP_SECURITY_SUBSCRIPTION_USE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates security subscription usage data per customer, specifically tracking the activation status and first/last activation dates for e-post verification, credit card monitoring, and VPN token creation actions.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_CCM_AGRM_SFTY_USE]]
| Column Name |
|---|
| KURT_ID |
| ACTION_DESCRIPTION |
| FIRST_DATE |
| LAST_DATE |

