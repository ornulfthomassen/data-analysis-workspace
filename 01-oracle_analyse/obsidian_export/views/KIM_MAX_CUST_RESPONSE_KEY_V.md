# KIM_MAX_CUST_RESPONSE_KEY_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the maximum customer response key from the KIM_CUSTOMER_RESPONSE table, excluding entries from source system key '94'. Returns 0 if no matching records are found.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| source_system_key |

