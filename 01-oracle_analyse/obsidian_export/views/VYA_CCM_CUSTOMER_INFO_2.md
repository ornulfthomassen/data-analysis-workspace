# VYA_CCM_CUSTOMER_INFO_2

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "VYA_CCM_CUSTOMER_INFO_2", consolidates comprehensive customer and product information by joining `CLM_CCM.CCM_CUSTOMER_INFO_2_V` with `CLM_ADM.ADM_CUSTOMER_MAPPING`. It calculates and assigns various customer and user profiles (e.g., 'Totalkunde', 'Mobilkunde', 'Fastnettkunde') for both consumer and business segments. These profiles are determined based on the types and quantities of products and services customers own or use, such as mobile subscriptions, fixed broadband, M2M devices, FWA, FBR, and TV services. The view also includes details on safety agreements, reward eligibility calculations, and an entry for a default 'unknown' customer (CUSTOMER_SK = -1), serving as a unified customer information source for analytical and reporting purposes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
| Column Name |
|---|
| KURT_ID |
| LOAD_DTTM |
| CLM_LIVSFASE_SEGMENT_ID |
| CLM_LIVSFASE_SEGMENT_NAME |
| CU_NO_UNITS_QUALIFIED_FB |
| CU_AGRMT_FB_STATUS |
| CU_AGRMT_FB_START_DTTM |
| CU_AGRMT_SFTY_STATUS |
| CU_AGRMT_SFTY_VALID_FROM_DATE |
| CU_AGRMT_SFTY_EMAIL_VERFY_DTTM |
| CU_AGRMT_SFTY_EMAIL_MONITORING |
| CU_AGRMT_SFTY_CC_DTTM |
| CU_AGRMT_SFTY_NO_ADD_CC_MON |
| CU_AGRMT_SFTY_VPN_VERFY_DTTM |
| CU_AGRMT_SFTY_NO_VPN_TOKEN |
| STATE_USER_MPP |
| CU_NO_MPP |
| CU_NO_MPR |
| CU_NO_FWA |
| CU_NO_FBR |
| CU_NO_TV_FTV |
| CU_NO_FBB_COAX |
| CU_NO_SWAP_AGREEMENT |
| CU_NO_MBB |
| CU_NO_MPP_USR |
| CU_NO_MPR_USR |
| CU_NO_FWA_USR |
| CU_NO_FBR_USR |
| CU_NO_TV_FTV_USR |
| CU_NO_FBB_COAX_USR |
| CU_NO_MBB_USR |
| CU_NO_MPP_BUS |
| CU_NO_FWA_BUS |
| CU_NO_MPP_BUS_USR |
| CU_NO_FWA_BUS_USR |
| CU_NO_MBB_BUS_USR |
| CU_NO_MPP_NEXT_ADULT |
| CU_NO_MPP_NEXT_U18 |
| CU_NO_MOB_TALKMORE |
| CU_NO_MOB_OTHER_SP |
| CU_NO_M2M_TRK |
| CU_NO_M2M_REST |
| CU_NO_FBB_FBR_FTV |
| CU_NO_FBB_FBR_FTV_USR |
| CU_NO_FIX_BBT_FTV |
| CU_NO_FIX_BBT_TNN |
| CU_NO_FBR_TNN |
| CU_NO_FBR_TNN_USR |
| CU_NO_DEVICE_AGREEMENT |
| CU_NO_DEVICE_INSURANCE |
| CU_NO_DEVICE_INSURANCE_CAMP |
- ← [[DUAL]]

