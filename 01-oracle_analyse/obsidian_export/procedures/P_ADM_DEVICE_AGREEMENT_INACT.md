# P_ADM_DEVICE_AGREEMENT_INACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_DEVICE_AGREEMENT_INACT`, populates a partitioned table named `ADM_DEVICE_AGREEMENT_INACTIVE` with detailed historical and current information about device agreements, their associated products, subscriptions, customer details, and IMEI usage for a specific period (month, determined by `P_YYYYMM`). It identifies various agreement and subscription change types (e.g., 'INNPORTERING', 'NYSALG', 'EIERSKIFTE', 'ANNET'). The procedure first creates a temporary table (`TMP_DEVICE_AGREEMENT_INACTIVE`), populates it with the aggregated data, and then uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently load this data into a new or existing partition of the permanent target table, `ADM_DEVICE_AGREEMENT_INACTIVE`, ensuring monthly data updates and historical tracking.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT]]

## Target Tables (Outputs)
- → [[TMP_DEVICE_AGREEMENT_INACTIVE]]
- → [[ADM_DEVICE_AGREEMENT_INACTIVE]]

