# VYA_ADM_ORDEN_ACTIVATION_SUBS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated dataset for 'Orden' product activation metrics associated with subscriptions. It links subscription offers and incentive data with historical activation records, calculating activation dates, flags, and the duration between activation availability and actual signup.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_ORDEN_ACTIVATION_HIST]]
| Column Name |
|---|
| DATE_ID |
| SIGNUP_DATE |
| START_FROM_DATE |
| SUBSCRIBED_COMPONENT_ID |
| LAST_FOREGROUND_TIME |
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SRC_SUBSCRIPTION_ID_1 |
| PRODUCT_OFFER_ID |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| INC_VALID_TO_DATE |
| PARAMETER_ID |
| PRODUCT_OFFER_ID |
| SUBSCRIBED_COMPONENT_ID |

