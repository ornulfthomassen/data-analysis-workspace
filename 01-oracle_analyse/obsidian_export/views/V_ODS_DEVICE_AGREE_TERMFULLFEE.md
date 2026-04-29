# V_ODS_DEVICE_AGREE_TERMFULLFEE

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts distinct agreement order details, including customer information (KURT_ID), account ID, and specific order parameters like status/type (PARAMETER_ID 1307 with values 'S' or 'P') and IMEI (PARAMETER_ID 8821). It filters for orders of type 770 that have arrived within the last 3 days.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| ORDER_ARRIVAL_DATE |
| INFO_REG_DATE |
| INFO_CHG_DATE |
| ORDER_TYPE_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
| Column Name |
|---|
| AGREEMENT_ORDER_COMPONENT_ID |
| AGREEMENT_ORDER_ID |
| AGREEMENT_ORDER_OFFER_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
| Column Name |
|---|
| PARAMETER_VALUE |
| AGREEMENT_ORDER_COMPONENT_ID |
| PARAMETER_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
| Column Name |
|---|
| AGREEMENT_ORDER_OFFER_ID |
| ACC_ID |
| CUST_ID |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| CUST_ID |

