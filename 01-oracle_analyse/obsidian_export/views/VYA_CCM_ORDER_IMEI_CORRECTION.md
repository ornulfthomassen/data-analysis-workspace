# VYA_CCM_ORDER_IMEI_CORRECTION

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies and tracks IMEI corrections made within customer agreements. It links original agreement orders with their corresponding correction orders, extracting old and new IMEI values, alongside relevant order and agreement identifiers and timestamps. Specifically, it looks for 'change' actions on orders and correlates parameters identified by specific IDs (8838 for old IMEI, 8821 for new IMEI).

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| AGREEMENT_ID |
| DEALER_ID |
| ORDER_ARRIVAL_DATE |
| AGREEMENT_ORDER_ID |
| ACTION_TYPE_ID |
| SALES_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| ACTION_TYPE_ID |
| AGREEMENT_ORDER_COMPONENT_ID |
| COMPONENT_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
| Column Name |
|---|
| AGREEMENT_ORDER_COMPONENT_ID |
| PARAMETER_ID |
| PARAMETER_VALUE |
| ACTION_TYPE_ID |

