# V_ODS_DEVICE_AGREE_UTEN_IMEI

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and retrieves active device agreements that are missing valid IMEI information (indicated by 'imei_full < 0'). It specifically filters for agreements with 'SRC_ROOT_PRODUCT_ID' equal to '770', an 'Original_Start_date' from January 1, 2019, up to 5 days before the current date, and an 'end_date' of '9999-12-31' (implying active agreements). The purpose is for reporting on these device agreements without IMEI through IMM and BI systems to KS.

## Data Sources (Inputs)
- ← [[ODS.AGREEMENT_ODS_MOB]]

