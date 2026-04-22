# P_ADM_DEVICE_AGREEMENT_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_DEVICE_AGREEMENT_KURT` is designed to create or refresh a monthly snapshot or aggregated view of device agreement data. It first performs a pre-check to validate the status of source data for the previous month (determined by `V_YYYYMM`). If the source data is deemed 'OK', the procedure manages previous versions of the target table (`ADM_DEVICE_AGREEMENT_KURT`) by renaming the existing one to a backup table (`ADM_DEVICE_AGREEMENT_KURT_OLD`). If an older backup exists or an overwrite is explicitly requested, it may drop the old backup. The core functionality involves creating a new `ADM_DEVICE_AGREEMENT_KURT` table by executing a `CREATE TABLE AS SELECT` statement. This statement joins numerous tables across various schemas to compile comprehensive information related to device agreements, subscriptions, products, and IMEI usage for the specified month. Finally, it gathers statistics on the newly created table and logs the process status.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CRM_ANALYSE.TDM_MOBIL_SUBSCR_HIST]]
- ← [[ADM_SUBSCRIPTION_HIST_KURT]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]

## Target Tables (Outputs)
- → [[ADM_DEVICE_AGREEMENT_KURT]]
- → [[ADM_DEVICE_AGREEMENT_KURT_OLD]]

