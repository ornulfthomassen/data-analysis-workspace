# P_ADM_CONNECT_ID_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Populates monthly partitions of three history tables (`ADM_CONNECT_ID_HIST`, `ADM_CONNECT_ID_SUBSCR_HIST`, and `ADM_CONNECT_ID_CUST_HIST`). It first aggregates and transforms data from various administrative and core system tables (`ADM_MONTH_DIM`, `SUBSCRIPTION`, `SUBSCRIBED_OFFER_CONFIGURATION`, `SUBSCRIPTION_MAPPING`, `ADM_SUBSCRIPTION_HISTORY`, `ADM_SUBSCRIPTION_HISTORY_I`) into a temporary table, which is then exchanged into the `ADM_CONNECT_ID_HIST` partition. Subsequently, subscription and customer history data are derived from the newly created `ADM_CONNECT_ID_HIST` partition and similarly loaded into `ADM_CONNECT_ID_SUBSCR_HIST` and `ADM_CONNECT_ID_CUST_HIST` partitions respectively. The procedure includes logic for partition creation, existence checks, and optional overwrite handling.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |
| FIRST_DATE |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |
| SUBSCR_ID |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| PARAMETER_VALUE |
| SUBSCR_ID |
| INFO_IS_DELETED |
| PARAMETER_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| SUBSCR_OFFER_CONFIG_PROD_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_USER |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_LAST_USER |
- ← [[CLM_ADM.ADM_CONNECT_ID_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| CUSTOMER_SK |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CONNECT_ID]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| CUSTOMER_SK |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| SUBSCR_OFFER_CONFIG_PROD_ID |
- → [[CLM_ADM.ADM_CONNECT_ID_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| CUSTOMER_SK |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
| SUBSCR_OFFER_CONFIG_PROD_ID |
- → [[CLM_ADM.TMP_CONNECT_ID_SUBS]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
- → [[CLM_ADM.ADM_CONNECT_ID_SUBSCR_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| SUBSCRIPTION_ID |
| SUBSCR_ID |
- → [[CLM_ADM.TMP_CONNECT_ID_CUST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| CUSTOMER_SK |
- → [[CLM_ADM.ADM_CONNECT_ID_CUST_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CONNECT_ID |
| CUSTOMER_SK |

