# V_ORDER_USER_AGE

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the age of the user at the time of each order line by joining order detail facts with customer dimensions.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
| Column Name |
|---|
| ORDER_LINE_KEY |
| ORDER_DT_KEY |
| USER_CUSTOMER_KEY |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| DATE_OF_BIRTH |
| CUSTOMER_KEY |

