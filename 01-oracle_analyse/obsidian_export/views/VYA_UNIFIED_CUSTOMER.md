# VYA_UNIFIED_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_UNIFIED_CUSTOMER, provides a comprehensive unified profile for business customers ('FORETAK'). It aggregates product subscription details (such as TV, broadband, and telephony for mobile and fixed services) from detailed subscription facts, along with customer demographics, address information, credit profiles, and segmentation details from customer dimensions. It also incorporates aggregated household-level product counts where applicable, offering a consolidated view of a business customer's services and associated individual user and household product metrics.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| USER_CUSTOMER_KEY |
| PRIM_PRODUCT_KEY |
| MARKET_AREA_KEY |
| SUBSCR_TYPE_STATUS_KEY |
| SUB_PRODUCT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[GALAXY.CUSTOMER_DIM_MV]]
| Column Name |
|---|
| CUSTOMER_KEY |
| CUSTOMER_CATEGORY |
| COMMERSIAL_CUSTOMER_NAME |
| ORGANISATION_NUMBER |
| MAIN_ADDRESS_MUNICIPAL_NUMBER |
| MAIN_ADDRESS_MUNICIPAL |
| MAIN_ADDRESS_COUNTY_NUMBER |
| MAIN_ADDRESS_COUNTY |
| COM_CUSTOMER_EMPLOYEES |
| CURRENT_CREDITPROFILE_DESC |
| CURRENT_SERVICE_CONCEPT |
| COM_CUSTOMER_COMPANY_TYPE |
| COM_CUSTOMER_ORG_ROLE_KURT |
| COM_CUSTOMER_SEGMENT |
| COM_CUSTOMER_PORTFOLIO |
| COM_CUSTOMER_SEGMENT_GROUP |
| COUNTERPART_KEY |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| CUSTOMER_ID |
- ← [[GALAXY.CUSTOMER_RELATION_PROFILE_FACT]]
| Column Name |
|---|
| NUM_MOBILE_TELEPHONY |
| NUM_FTV_FIXED_TV |
| NUM_FTV_FIXED_BROADBAND_COAX |
| NUM_FTV_FIXED_BROADBAND_FIBER |
| NUM_FIXED_BROADBAND_ADSL |
| NUM_FIXED_BROADBAND_FIBER |
| NUM_FIXED_BROADBAND_VDSL |
| CUSTOMER_KEY |
| CURRENT_STATUS |
| NUM_MOBILE_TELEPHONY_PREPAID |
| NUM_MOBILE_BROADBAND |
| NUM_MOBILE_TELEMETRY |
| NUM_SWAP |
| NUM_SWAP_PLUS_INSURANCE |
| FAMILY_BONUS_FLAG |
| DATABONUS_GB |
| SECUREID_FLAG |
| NUM_FTV_FIXED_TELEPHONY_BBT |
| NUM_FIXED_TELEPHONY_ISDN |
| NUM_FIXED_TELEPHONY_PSTN |
| NUM_FIXED_TELEPHONY_BBT |
- ← [[GALAXY.COUNTERPART_DIM]]
| Column Name |
|---|
| CP_CLASSIFICATION_DESC |
| COUNTERPART_KEY |

