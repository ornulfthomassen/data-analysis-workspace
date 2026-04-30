# V_ADM_MONTH_SUBSI_CUST_HH

**Schema:** `CCM` | **Type:** `View`

## Description
This view generates a monthly aggregated dataset combining subscription history with associated customer and household information from various administrative tables. It calculates unique keys for period, subscription, main ID, customer, and household, providing both current month and next month derivatives. The view filters out specific test/internal customer records to ensure data quality for analytical purposes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_KEY_CHAR |
| LAST_DATE |

- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_LAST_USER |

- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |

- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| CUSTOMER_SK |
| PERIOD_MONTH_KEY |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |


