# V_ODS_AGRM_DEVICE

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_ODS_AGRM_DEVICE, consolidates detailed information about 'Utstyr' (equipment/device) agreements, linking them to customer data and specific mobile device (IMEI) usage history. It retrieves agreement details, product specifics, customer mapping, and the latest terminal usage dates for IMEIs. It also derives flags to indicate whether an agreement, product, or IMEI (based on recent usage) is active.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
- ← [[clm_ccm.v_ods_agrmt_offer_mob_device]]
- ← [[clm_adm.adm_customer_mapping]]
- ← [[live.eureka_imei]]

